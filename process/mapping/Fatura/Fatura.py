from process.util import extract_value

class FaturaNFe:
    def __init__(self, item):

        self.numero_fatura = extract_value(item, "./nFat")
        self.valor_original = extract_value(item, "./vOrig")
        self.valor_desconto = extract_value(item, "./vDesc")
        self.valor_liquido = extract_value(item, "./vLiq")

    def to_dict(self):
        return self.__dict__
