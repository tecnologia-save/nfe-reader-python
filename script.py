from pprint import pprint
from lxml import etree

from process.handler.EntidadeHandler import EntidadeHandler
from process.handler.FaturaHandler import FaturaHandler
from process.handler.NotaFiscalHandler import NotaFiscalHandler
from process.handler.ProdutosHandler import ProdutosHandler
from process.handler.ResponsavelTecnicoHandler import ResponsavelTecnicoHandler
from process.handler.TotaisHandler import TotaisHandler
from process.handler.TransporteHandler import TransporteHandler
from process.util import remove_namespaces
import os
from batch_save.save_nfe import save_dicts

from tqdm import tqdm
import concurrent.futures
import time



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

    return nfe


def safe_process(file_path):
    try:
        return process(file_path)
    except Exception as e:
        # Aqui você pode registrar/logar o erro, se desejar
        return None


if __name__ == '__main__':
    directory = '/home/vinicius/Documents/nfe-reader-python/test/files2'

    files = [os.path.join(directory, file) for file in os.listdir(directory)]

    notas = []

    for file in tqdm(files):
        
        notas.append(process(file))



    start = time.time()
    save_dicts(notas_fiscais_originais=notas)
    end = time.time()

    print(f"Tempo inserção de {len(notas)} linhas: {end - start}")