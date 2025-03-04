from pprint import pprint
from lxml import etree

from process.handler.EntidadeHandler import EntidadeHandler
from process.handler.FaturaHandler import FaturaHandler
from process.handler.NotaFiscalHandler import NotaFiscalHandler
from process.handler.ProdutosHandler import ProdutosHandler
from process.handler.ResponsavelTecnicoHandler import ResponsavelTecnicoHandler
from process.handler.TotaisHandler import TotaisHandler
from process.handler.TransporteHandler import TransporteHandler
from batch_save.validate_nfs import ValidateNFs
from process.util import remove_namespaces

from batch_save.save_nfe import save_dicts
from batch_save.db_operations import DB

from tqdm import tqdm

import os
import time
import json
from datetime import datetime

def process(file) -> dict:
    tree = etree.parse(file)
    root = remove_namespaces(tree)
    nfe = dict()

    nfe.update(EntidadeHandler(root).process())
    nfe.update(NotaFiscalHandler(root).process())
    nfe.update(ProdutosHandler(root).process())
    nfe.update(TotaisHandler(root).process())
    nfe.update(FaturaHandler(root).process())
    nfe.update(TransporteHandler(root).process())
    nfe.update(ResponsavelTecnicoHandler(root).process())

    nfe['nome_arquivo'] = [file.split('/')[-1]]

    return nfe


def safe_process(file_path):
    try:
        return process(file_path)
    except Exception as e:
        return None


if __name__ == '__main__':
    directory = '/home/vinicius/Documents/nfe-reader-python/test/files2'

    files = [os.path.join(directory, file) for file in os.listdir(directory)]

    list_controle_importacao = []


    notas = []
    for file in tqdm(files):        
        notas.append(process(file))


    start = time.time()


    validate_nfs = ValidateNFs(notas)
    notas_validas, notas_invalidas = validate_nfs.validate()

    controle_importacao_notas_validas = []
    controle_importacao_notas_invalidas = []

    for nota_valida in notas_validas:
        emitente = nota_valida.get('emitente')
        if emitente:
            print(emitente)
            cnpj = emitente.get('cgc')
        else:
            cnpj = ''

        controle_importacao_notas_validas.append({
                'nome_arquivo': nota_valida['nome_arquivo'][0], 
                'status': '1', 
                'tipo_importacao': '1', 
                'descricao_erros': f"{nota_valida}", 
                'cliente': '1', 
                'created_by': '1', 
                'created_at': datetime.now(), 
                'updated_at': datetime.now(),
                'dados': json.dumps({"cnpj": cnpj}) 
            })
        
    for nota_invalida in notas_invalidas:
        emitente = nota_invalida.get('emitente')
        if emitente:
            cnpj = emitente.get('cgc')
        else: 
            cnpj = ''
        controle_importacao_notas_invalidas.append({
                'nome_arquivo': nota_invalida['nota_fiscal']['nome_arquivo'][0], 
                'status': '2', 
                'tipo_importacao': '1', 
                'descricao_erros': f"{nota_invalida['mensagem']} - {nota_invalida['nota_fiscal']}", 
                'cliente': '1', 
                'created_by': '1', 
                'created_at': datetime.now(), 
                'updated_at': datetime.now(),   
                'dados': json.dumps({"cnpj": cnpj}) 
            })

    end = time.time()

    print(f"Tempo validações: {end - start}")


    start = time.time()

    with DB() as db:
        ids_nomes_salvos = db.save_all(controle_importacao_notas_validas, 'controle_importacao', returning_values='id, nome_arquivo', clear_complex_values=False)
        db.save_all(controle_importacao_notas_invalidas, 'controle_importacao', clear_complex_values=False)

    mapa_nome_id = {nome_arquivo: id for id, nome_arquivo in ids_nomes_salvos}
    
    for nota in notas_validas:
        nome_arquivo = nota['nome_arquivo'][0]
        if nome_arquivo in mapa_nome_id:
            nota['controler_importacao'] = mapa_nome_id[nome_arquivo]  # Atribuir ID

    save_dicts(notas_validas)
    
    end = time.time()

    print(f"Tempo inserção de {len(notas)} linhas: {end - start}")