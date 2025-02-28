from lxml import etree

from process.handler.EntidadeHandler import EntidadeHandler
from process.handler.FaturaHandler import FaturaHandler
from process.handler.NotaFiscalHandler import NotaFiscalHandler
from process.handler.ProdutosHandler import ProdutosHandler
from process.handler.ResponsavelTecnicoHandler import ResponsavelTecnicoHandler
from process.handler.TotaisHandler import TotaisHandler
from process.handler.TransporteHandler import TransporteHandler
from save.main import SaveNotaFiscal
from process.util import remove_namespaces
from controle_importacao import update_controle_importacao, insert_controle_importacao
import json
import os
import boto3
import psycopg2
import urllib.parse
import traceback

s3Client = boto3.client('s3')



def process(file) -> dict:
    tree = etree.fromstring(file)
    root = remove_namespaces(tree)
    nfe = dict()

    nfe.update(EntidadeHandler(root).process())
    nfe.update(NotaFiscalHandler(root).process())
    nfe.update(ProdutosHandler(root).process())
    nfe.update(TotaisHandler(root).process())
    nfe.update(FaturaHandler(root).process())
    nfe.update(TransporteHandler(root).process())
    nfe.update(ResponsavelTecnicoHandler(root).process())

    return nfe




def lambda_handler(event, context):

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    file_key = urllib.parse.unquote(file_key).replace("+", " ")

    print(f"Bucket: {bucket_name}, File: {file_key}")
    cliente, created_by = get_client_created_by(file_key)

    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_DATABASE'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )
    cursor = conn.cursor()

    controle_id = insert_controle_importacao(
        cursor,
        conn,
        nome_arquivo=file_key.split("/")[-1],
        status=4,
        tipo_importacao=1,
        cliente=cliente,
        created_by=created_by
    )

    nota_fiscal_dict = None
    cnpj = None
    try:
        s3_file = s3Client.get_object(Bucket=bucket_name, Key=file_key)
        xml_content = s3_file['Body'].read()
        nota_fiscal_dict = process(xml_content)
        cnpj = nota_fiscal_dict['emitente']['cgc']
    except Exception as e:
        stack_trace = traceback.format_exc()
        print(f"Erro ao processar: {e} -- {stack_trace}")
        if conn:
            conn.rollback()  # Reverte a transação
        update_controle_importacao(
            cursor,
            conn,
            controle_id,
            status=2,
            descricao_erros=f"{e} -- {stack_trace}",
            dados={'cnpj': cnpj, 'nota_fiscal': nota_fiscal_dict}
        )



    try:

        update_controle_importacao(
            cursor,
            conn,
            controle_id,
            status=1,
            dados={'cnpj': cnpj, 'nota_fiscal': nota_fiscal_dict}
        ) 

        if controle_id is None:
            raise Exception("Falha ao inserir controle de importação.")


        save_nota_fiscal = SaveNotaFiscal(nota_fiscal_dict, {"created_by": created_by, "cliente": cliente}, controle_id, conn, cursor)
        save_nota_fiscal.save()
        
    except Exception as e:
        stack_trace = traceback.format_exc()
        print(f"Erro ao salvar: {e} -- {stack_trace}")
        if conn:
            conn.rollback()  # Reverte a transação
        update_controle_importacao(
            cursor,
            conn,
            controle_id,
            status=2,
            descricao_erros=f"{e} -- {stack_trace}",
            dados={'cnpj': cnpj, 'nota_fiscal': nota_fiscal_dict}
        )
    finally:
        if conn:
            conn.commit()
            cursor.close()
            conn.close()



def get_client_created_by(file_key):
    paths = file_key.split("/")
    return paths[1], paths[3]