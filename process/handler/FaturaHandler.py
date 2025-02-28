from process.mapping.Fatura.Duplicatas import Duplicatas
from process.mapping.Fatura.Fatura import FaturaNFe


class FaturaHandler:
    def __init__(self, root):
        self.root = root

    def process(self):
        cobr = self.root.xpath(".//cobr")
        if cobr:
            cobr = cobr[0]
            fat_tree = cobr.find("./fat")
            if fat_tree is not None:
                fat = FaturaNFe(fat_tree)
                fat_dict = fat.to_dict()

                duplicatas = [
                    Duplicatas(dup).to_dict() for dup in cobr.findall("./dup")
                ]
                if duplicatas:
                    fat_dict.update(duplicatas=duplicatas)

                return {"fatura": fat_dict}
        return {}