from process.util import extract_value

class TotalISSQ:
    def __init__(self, item):
        self.valor_total_servicos_nao_tributados_icms = extract_value(item, "./vServ")
        self.base_calculo_issq = extract_value(item, "./vBC")
        self.valor_total_issq = extract_value(item, "./vISS")
        self.valor_total_pis = extract_value(item, "./vPIS")
        self.valor_total_cofins = extract_value(item, "./vCOFINS")
        self.valor_deducao_reducao_base_calculo = extract_value(item, "./vDeducao")
        self.valor_outras_retencoes = extract_value(item, "./vOutro")
        self.valor_desconto_incondicionado = extract_value(item, "./vDescIncond")
        self.valor_desconto_condicionado = extract_value(item, "./vDescCond")
        self.valor_total_retencao_issq = extract_value(item, "./vISSRet")
        self.data_prestacao_servico = extract_value(item, "./dCompet")
        self.codigo_regime_especial_tributacao = extract_value(item, "./cRegTrib")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__