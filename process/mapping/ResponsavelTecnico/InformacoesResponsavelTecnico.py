from process.util import extract_value

class InformacoesResponsavelTecnico:
    def __init__(self, item):
        self.cnpj = extract_value(item, "./CNPJ")
        self.contato = extract_value(item, "./xContato")
        self.email = extract_value(item, "./email")
        self.telefone = extract_value(item, "./fone")
    def to_dict(self):
        return self.__dict__
