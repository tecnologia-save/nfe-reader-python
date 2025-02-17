from process.util import extract_value

class ISSQN:
    def __init__(self, item):

        self.valor_da_base_de_calculo = extract_value(item, "./vBC")
        self.valor_aliquota_do_isssqn = extract_value(item, "./vISSQN")
        self.valor_deducao = extract_value(item, "./vDeducao")
        self.valor_outras_retencoes = extract_value(item, "./vOutro")
        self.valor_desconto_condicionado = extract_value(item, "./vDescCond")
        self.valor_desconto_incondicionado = extract_value(item, "./vDescIncond")
        self.valor_de_iss_retido = extract_value(item, "./vISSRet")
        self.indicador_de_iss_retido = extract_value(item, "./indISS")
        self.codigo_municipio_gerador_do_issqn = extract_value(item, "./cMunFG")
        self.codigo_item_lista_servicos = extract_value(item, "./cListServ")
        self.codigo_servico = extract_value(item, "./cServico")
        self.codigo_municipio = extract_value(item, "./cMun")
        self.codigo_pais = extract_value(item, "./cPais")
        self.numero_processo = extract_value(item, "./nProcesso")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__