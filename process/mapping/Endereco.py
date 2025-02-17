from process.util import extract_value
class Endereco:
    def __init__(self, item):
        self.logradouro = extract_value(item, "./xLgr")
        self.numero = extract_value(item, "./nro")
        self.complemento = extract_value(item, "./xCpl")
        self.bairro = extract_value(item, "./xBairro")
        self.codigo_municipio = extract_value(item, "./cMun")
        self.nome_municipio = extract_value(item, "./xMun")
        self.codigo_pais = extract_value(item, "./cPais")
        self.nome_pais = extract_value(item, "./xPais")
        self.cep = extract_value(item, "./CEP")
        self.uf = extract_value(item, "./UF")
        self.fone = extract_value(item, "./fone")
        self.email = extract_value(item, "./email")

    def to_dict(self):
        return self.__dict__