from process.mapping.Imposto import II
from process.mapping.Imposto.COFINS import COFINS
from process.mapping.Imposto.COFINSST import COFINSST
from process.mapping.Imposto.ICMS import ICMS
from process.mapping.Imposto.IPI import IPI
from process.mapping.Imposto.ISSQN import ISSQN
from process.mapping.Imposto.ImpostoDevolucao import ImpostoDevolucao
from process.mapping.Imposto.PIS import PIS
from process.mapping.Produto.ProdutoItem import ProdutoItem
from process.util import extract_value


class ProdutosHandler:
    def __init__(self, root):
        self.root = root

    def process(self):
        produtos = []
        for det in self.root.xpath(".//det"):
            produto_item = ProdutoItem(det.find("./prod"))
            produto_dict = produto_item.to_dict()

            # Processar impostos relacionados ao produto
            impostos = self.process_impostos(det)
            produto_dict.update({'imposto': impostos})

            produtos.append(produto_dict)
        return {"produtos": produtos}

    def process_impostos(self, det):
        impostos = {}

        imposto = det.find(f"./imposto")
        valor_total_tributos = extract_value(imposto, "./cProd")

        impostos.update({'valor_total_tributos': valor_total_tributos})

        mappings = {
            "COFINS": COFINS,
            "ICMS": ICMS,
            "PIS": PIS,
            "COFINSST": COFINSST,
            "ISSQN": ISSQN,
            "II": II,
            "IPI": IPI,
            "impostoDevol": ImpostoDevolucao,
        }

        for imposto_tag, imposto_class in mappings.items():
            imposto_elem = det.find(f"./imposto/{imposto_tag}")
            if imposto_elem is not None:
                grupo = [child.tag for child in imposto_elem]
                impostos[imposto_tag.lower()] = imposto_class(imposto_elem, grupo[0]).to_dict()



        mappings = {
            "cofins": "cofins_produto",
            "icms": "icms_produto",
            "pis": "pis_produto",
            "cofinsst": "cofins_st_produto",
            "issqn": "issqn_produto",
            "ii": "imposto_importacao_produto",
            "ipi": "ipi_produto",
            "impostodevolucao": "imposto_devolucao_produto"
        }


        for imposto in list(impostos.keys()):
            if imposto in mappings:
                impostos[mappings[imposto]] = impostos.pop(imposto)

        return impostos