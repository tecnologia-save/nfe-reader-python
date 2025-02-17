from process.util import extract_value

class Importacao:
    def __init__(self, item):
        self.valor_base_imposto_importacao = extract_value(item, "./vBC")
        self.valor_das_despesas_aduaneiras = extract_value(item, "./vDespAdu")
        self.valor_imposto_importacao = extract_value(item, "./vII")
        self.valor_iof = extract_value(item, "./vIOF")

    def to_dict(self):
        return self.__dict__
