
from process.util import extract_value

class ProdutoItem():
    def __init__(self, item):
        """
        Inicializa a classe ProdutoItem extraindo valores do XML.

        Args:
            item: Elemento XML contendo os dados do produto.
            created_by: ID do usuário que criou o registro.
            cliente: ID do cliente associado ao registro.
        """
        self.codigo_produto = extract_value(item, "./cProd")
        self.codigo_barras_gtin = extract_value(item, "./cEAN")
        self.codigo_barras = extract_value(item, "./cBarra")
        self.descricao_produto = extract_value(item, "./xProd")
        self.ncm = extract_value(item, "./NCM")
        self.ex_tipi = extract_value(item, "./EXTIPI")
        self.unidade_comercial = extract_value(item, "./uCom")
        self.gtin_unidade = extract_value(item, "./cEANTrib")
        self.codigo_barras_unidade_tributavel = extract_value(item, "./cBarraTrib")
        unidade_tributavel = extract_value(item, "./uTrib")
        self.unidade_tributavel = unidade_tributavel if unidade_tributavel else '' 
        self.quantidade_comercial = extract_value(item, "./qCom")
        self.valor_unitario_comercial = extract_value(item, "./vUnCom")
        self.valor_total_bruto = extract_value(item, "./vProd")
        self.quantidade_tributavel = extract_value(item, "./qTrib")
        self.valor_unitario_tributavel = extract_value(item, "./vUnTrib")
        self.valor_total_frete = extract_value(item, "./vFrete")
        self.valor_total_seguro = extract_value(item, "./vSeg")
        self.valor_total_desconto = extract_value(item, "./vDesc")
        self.outras_despesas_acessorias = extract_value(item, "./vOutro")
        self.cfop = extract_value(item, "./CFOP")
        self.tipo_item = extract_value(item, "./nTipoItem")
        self.valor_compoe_total_nf = extract_value(item, "./indTot")
        self.destaca_produto_perigoso = extract_value(item, "./dProd")
        self.pedido_compra = extract_value(item, "./xPed")
        self.numero_item_pedido_compra = extract_value(item, "./nItemPed")
        self.ficha_conteudo_importacao = extract_value(item, "./nFCI")
        self.numero_do_recopi = extract_value(item, "./nRECOPI")
        self.codigo_cest = extract_value(item, "./CEST")
        self.indicador_escala_relevante = extract_value(item, "./indEscala")
        self.cnpj_fabricante = extract_value(item, "./CNPJFab")
        self.codigo_beneficio_fiscal_uf = extract_value(item, "./cBenef")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
