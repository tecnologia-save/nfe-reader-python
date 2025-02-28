from process.util import extract_value

class IPI:
    def __init__(self, item,grupo):

        self.codigo_de_enquadramento_legal = extract_value(item, "./cEnq")
        self.cnpj_produtor = extract_value(item, "./CNPJProd")
        self.codigo_selo = extract_value(item, "./cSelo")
        self.quantidade_selo = extract_value(item, "./qSelo")
        self.codigo_enquadramento_para_cigarros_bebidas = extract_value(item, "./cIEnq")

        # Identificar e processar o grupo de classificação (IPI Tributado ou Não Tributado)
        self.get_grupo_classificacao_epi(item)

    def get_grupo_classificacao_epi(self, item):
        """
        Identifica e processa a classificação do IPI (Tributado ou Não Tributado).

        Args:
            item: Elemento XML contendo o grupo IPI.
        """
        ipi_tributado = item.find("./IPITrib")
        ipi_nao_tributado = item.find("./IPINT")

        if ipi_tributado is not None:
            self.set_imposto_produtos_industrializados_tributado(ipi_tributado)
        elif ipi_nao_tributado is not None:
            self.set_imposto_produtos_industrializados_nao_tributado(ipi_nao_tributado)

    def set_imposto_produtos_industrializados_tributado(self, ipi_tributado):
        """
        Configura os valores para o grupo IPI Tributado.

        Args:
            ipi_tributado: Elemento XML contendo os dados do IPI Tributado.
        """
        self.codigo_situacao_tributaria = extract_value(ipi_tributado, "./CST")
        self.valor_bc_ipi = extract_value(ipi_tributado, "./vBC")
        self.aliquota_ipi = extract_value(ipi_tributado, "./pIPI")
        self.valor_ipi_ser_pago = extract_value(ipi_tributado, "./vIPI")
        self.ipi_tributado = True

    def set_imposto_produtos_industrializados_nao_tributado(self, ipi_nao_tributado):
        """
        Configura os valores para o grupo IPI Não Tributado.

        Args:
            ipi_nao_tributado: Elemento XML contendo os dados do IPI Não Tributado.
        """
        self.codigo_situacao_tributaria = extract_value(ipi_nao_tributado, "./CST")
        self.ipi_tributado = False

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
