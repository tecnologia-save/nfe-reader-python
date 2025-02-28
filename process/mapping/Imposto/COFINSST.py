from process.util import extract_value

class COFINSST():
    def __init__(self, item):
        """
        Inicializa a classe COFINSST extraindo valores do XML.

        Args:
            item: Elemento XML contendo os dados do COFINS ST.
            produto: ID do produto associado.
            nota_fiscal: ID da nota fiscal associada.
            cliente: ID do cliente associado.
            created_by: ID do usuário que criou o registro.
        """
        self.valor_da_base_de_calculo = extract_value(item, "./vBC")
        self.percentual_aliquota_do_cofins = extract_value(item, "./pCOFINS")
        self.valor_do_cofins = extract_value(item, "./vCOFINS")
        self.quantidade_vendida = extract_value(item, "./qBCProd")
        self.aliquota_do_cofins_em_reais = extract_value(item, "./vAliqProd")
        self.valor_soma_cofins_compoe_total_nota = extract_value(item, "./indSomaCOFINSST", bool)

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
