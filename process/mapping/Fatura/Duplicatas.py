from process.util import extract_value

class Duplicatas:
    def __init__(self, item):
        self.valor_duplicata = extract_value(item, "./vDup")
        self.data_vencimento = extract_value(item, "./dVenc")
        self.numero_duplicata = extract_value(item, "./nDup")

    def to_dict(self):
        return self.__dict__
