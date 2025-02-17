from process.util import extract_value

class COFINS():
    def __init__(self, item, grupo):
        """
        Inicializa a classe COFINS extraindo valores do XML.

        Args:
            item: Elemento XML contendo os dados do COFINS.
            grupo: Grupo do COFINS.
            produto: ID do produto associado.
            nota_fiscal: ID da nota fiscal associada.
            cliente: ID do cliente associado.
            created_by: ID do usuário que criou o registro.
        """
        
        self.grupo = grupo.lower()
        self.codigo_situacao_tributaria = extract_value(item, f"./{grupo}/CST")
        self.valor_da_base_de_calculo = extract_value(item, f"./{grupo}/vBC")
        self.percentual_aliquota_do_cofins = extract_value(item, f"./{grupo}/pCOFINS")
        self.valor_do_cofins = extract_value(item, f"./{grupo}/vCOFINS")
        self.quantidade_vendida = extract_value(item, f"./{grupo}/qBCProd")
        self.aliquota_do_cofins_em_reais = extract_value(item, f"./{grupo}/vAliqProd")
        self.valor_soma_cofins_compoe_total_nota = extract_value(item, f"./{grupo}/indSomaCOFINSST")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
