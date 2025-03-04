from lxml import etree

from process.handler.EntidadeHandler import EntidadeHandler
from process.handler.FaturaHandler import FaturaHandler
from process.handler.NotaFiscalHandler import NotaFiscalHandler
from process.handler.ProdutosHandler import ProdutosHandler
from process.handler.ResponsavelTecnicoHandler import ResponsavelTecnicoHandler
from process.handler.TotaisHandler import TotaisHandler
from process.handler.TransporteHandler import TransporteHandler
from process.util import remove_namespaces
import boto3
import urllib.parse

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

    nota_fiscal_dict = None
    cnpj = None
    s3_file = s3Client.get_object(Bucket=bucket_name, Key=file_key)
    xml_content = s3_file['Body'].read()
    nota_fiscal_dict = process(xml_content)
    cnpj = nota_fiscal_dict['emitente']['cgc']

    nota_fiscal_dict['cliente'] = cliente
    nota_fiscal_dict['created_by'] = created_by
    nota_fiscal_dict['nome_arquivo'] = [file_key.split("/")[-1]]

    return nota_fiscal_dict


def get_client_created_by(file_key):
    paths = file_key.split("/")
    return paths[1], paths[3]