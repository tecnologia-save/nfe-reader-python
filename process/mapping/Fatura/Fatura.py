from process.util import extract_value

class FaturaNFe:
    def __init__(self, item):

        self.numero_fatura = extract_value(item, "./nFat")
        self.valor_original = extract_value(item, "./vOrig")

        valor_desconto = extract_value(item, "./vDesc")
        self.valor_desconto = valor_desconto if valor_desconto else 0

        self.valor_liquido = extract_value(item, "./vLiq")

    def to_dict(self):
        return self.__dict__
