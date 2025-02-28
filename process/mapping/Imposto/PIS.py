from process.util import extract_value

class PIS:
    def __init__(self, item, grupo):
        self.grupo = grupo
        self.codigo_situacao_tributaria = extract_value(item, f"./{grupo}/CST")
        self.valor_da_base_de_calculo = extract_value(item, f"./{grupo}/vBC")
        self.percentual_aliquota_do_pis = extract_value(item, f"./{grupo}/pPIS")
        self.valor_do_pis = extract_value(item, f"./{grupo}/vPIS")
        self.quantidade_vendida = extract_value(item, f"./{grupo}/qBCProd")
        self.aliquota_do_pis_em_reais = extract_value(item, f"./{grupo}/vAliqProd")
        self.valor_soma_pis_compoe_total_nota = extract_value(item, f"./{grupo}/indSomaPISST")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
