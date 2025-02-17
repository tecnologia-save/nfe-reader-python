from process.mapping.Totais.TotalICMS import TotalICMS
from process.mapping.Totais.TotalISSQ import TotalISSQ
from process.mapping.Totais.TotalRetencaoTributosFederais import TotalRetencaoTributosFederais


class TotaisHandler:
    def __init__(self, root):
        self.root = root

    def process(self):
        totais = {}

        total_mappings = {
            "ICMSTot": TotalICMS,
            "ISSQN": TotalISSQ,
            "retTrib": TotalRetencaoTributosFederais,
        }

        for tag, total_class in total_mappings.items():
            total_tree = self.root.xpath(f".//{tag}")
            if total_tree:
                total_obj = total_class(total_tree[0])
                totais.update({f"total_{tag.lower()}": total_obj.to_dict()})

        return {"totais": totais}