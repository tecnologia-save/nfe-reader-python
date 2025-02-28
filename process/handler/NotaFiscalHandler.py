from process.mapping.NotaFiscal import NotaFiscal

class NotaFiscalHandler:
    def __init__(self, root):
        self.root = root

    def process(self):
        if self.root is not None:

            to_read = self.root.xpath(".//infCFe")
            type = 'cfe'

            if not to_read:
                to_read = self.root.xpath(".//infNFe")
                type = 'nfe'

            if to_read:
                to_read = to_read[0]

            nota = NotaFiscal(to_read, type)

        if nota:
            return nota.to_dict()
        else:
            return {}