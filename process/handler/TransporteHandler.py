from process.mapping.Transporte.TransporteNfe import TransporteNfe


class TransporteHandler:
    def __init__(self, root):
        self.root = root

    def process(self):
        transp_tree = self.root.xpath(".//transp")
        if transp_tree:
            transp = TransporteNfe(transp_tree[0])
            return {"transp": transp.to_dict()}
        return {}