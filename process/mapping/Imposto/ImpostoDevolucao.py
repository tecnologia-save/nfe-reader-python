from process.util import extract_value

class ImpostoDevolucao:
    def __init__(self, item):
        self.percentual_de_mercadoria_devolvida = extract_value(item, "./pDevol")
        self.valor_do_ipi_devolvido = extract_value(item, "./IPI/vIPIDevol")

    def to_dict(self):
        return self.__dict__
