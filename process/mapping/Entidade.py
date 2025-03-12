from process.mapping.Endereco import Endereco
from process.util import extract_value
class Entidade:
    def __init__(self, emit):
        """
        Inicializa a classe Entidade extraindo valores do XML.

        Args:
            emit: Elemento XML contendo os dados do emitente.
        """
        self.cgc = extract_value(emit, "./CNPJ") or extract_value(emit, "./CPF")
        self.nome = extract_value(emit, "./xNome")
        self.nome_fantasia = extract_value(emit, "./xFant")
        self.inscricao_estadual = extract_value(emit, "./IE")
        self.inscricao_municipal = extract_value(emit, "./IM")
        self.cnae = extract_value(emit, "./CNAE")
        self.codigo_regime_tributario = extract_value(emit, "./CRT")
        self.email = extract_value(emit, "./email")
        self.fone = extract_value(emit, "./fone")



        endereco = emit.find("./enderEmit")

        if endereco is None:
            endereco = emit.find("./enderDest")

        if endereco is not None:
            self.endereco = Endereco(endereco).to_dict()

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__