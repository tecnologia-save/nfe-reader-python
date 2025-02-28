from process.util import extract_value
from datetime import datetime
import re


class NotaFiscal():

    def __init__(self, nfe, type):

        # try:

        #     self.chave = nfe.attrib.get("Id")
        #     if self.chave:
        #         self.chave = re.sub(r'\D', '', self.chave)

        # except AttributeError:
        #     raise AttributeError("Atributo chave não encontrado. Verifique se o xml é válido")


        if type == 'nfe':
            self.numero_nfe = extract_value(nfe, "./ide/nNF")
            self.serie = extract_value(nfe, "./ide/serie")
            self.data_emissao = extract_value(nfe, "./ide/dhEmi")
        else:
            self.numero_nfe = extract_value(nfe, "./ide/nCFe")
            self.serie = extract_value(nfe, "./ide/nserieSAT")
            dEmi = extract_value(nfe, "./ide/dEmi")
            data_emissao = datetime.strptime(dEmi, "%Y%m%d").date()
            self.data_emissao = data_emissao.isoformat()






        natureza_operacao = extract_value(nfe, "./ide/natOp")

        self.natureza_operacao = natureza_operacao if natureza_operacao else ''
        self.data_saida_entrada = extract_value(nfe, "./ide/dhSaiEnt")
        self.versao_processo_emissao = extract_value(nfe, "./ide/verProc")
        self.codigo_numerico = extract_value(nfe, "./ide/cNF")
        self.cfop = extract_value(nfe, "./det/prod/CFOP")
        self.municipio_icms = extract_value(nfe, "./ide/cMunFG")
        self.Justificativa_entrada_contingencia = extract_value(nfe, "./ide/xJust")
        self.data_entrada_contingencia = extract_value(nfe, "./ide/dhCont")
        self.email_para_recebimento_arquivos = extract_value(nfe, "./dest/email")
        self.numero_pedido = extract_value(nfe, "./det/prod/xPed")
        self.uf = extract_value(nfe, "./ide/cUF")
        self.modelo_nfe = extract_value(nfe, "./ide/mod")
        self.tipo_operacao = extract_value(nfe, "./ide/tpNF")
        self.tipo_ambiente = extract_value(nfe, "./ide/tpAmb")
        self.local_destino_operacao = extract_value(nfe, "./ide/idDest")
        self.operacao_consumidor_final = extract_value(nfe, "./ide/indFinal")
        self.operacao_presenca_comprador = extract_value(nfe, "./ide/indPres")
        self.tipo_impressao = extract_value(nfe, "./ide/tpImp")
        self.tipo_emissao = extract_value(nfe, "./ide/tpEmis")
        self.finalidade_emissao = extract_value(nfe, "./ide/finNFe")
        self.processo_emissao = extract_value(nfe, "./ide/procEmi")
        self.digito_verificador = extract_value(nfe, "./ide/cDV")
        self.fuso_horario = extract_value(nfe, "./ide/fusoHorario")

        self.informacoes_adicionais_interesse_fisco = extract_value(nfe, "./infAdic/infAdFisco")
        self.informacoes_adicionais_contribuinte = extract_value(nfe, "./infAdic/infCpl")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
