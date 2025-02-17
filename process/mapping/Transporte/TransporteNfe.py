from process.util import extract_value

class ModalidadeFrete:
    CONTRATACAO_FRETE_POR_CONTA_REMETENTE = 0
    CONTRATACAO_FRETE_POR_CONTA_DESTINATARIO = 1
    CONTRATACAO_FRETE_POR_CONTA_TERCEIROS = 2
    TRANSPORTE_PROPRIO_POR_CONTA_REMETENTE = 3
    TRANSPORTE_PROPRIO_POR_CONTA_DESTINATARIO = 4
    SEM_OCORRENCIA_DE_TRANSPORTE = 9

    DESCRICOES = {
        CONTRATACAO_FRETE_POR_CONTA_REMETENTE: 'Contratação do Frete por conta do Remetente (CIF)',
        CONTRATACAO_FRETE_POR_CONTA_DESTINATARIO: 'Contratação do Frete por conta do Destinatário (FOB)',
        CONTRATACAO_FRETE_POR_CONTA_TERCEIROS: 'Contratação do Frete por conta de Terceiros',
        TRANSPORTE_PROPRIO_POR_CONTA_REMETENTE: 'Transporte Próprio por conta do Remetente',
        TRANSPORTE_PROPRIO_POR_CONTA_DESTINATARIO: 'Transporte Próprio por conta do Destinatário',
        SEM_OCORRENCIA_DE_TRANSPORTE: 'Sem Ocorrência de Transporte',
    }

    @staticmethod
    def get_descricao(codigo):
        return ModalidadeFrete.DESCRICOES.get(codigo, 'Código desconhecido')

class TransporteNfe:
    def __init__(self, item):

        self.modo_de_frete = extract_value(item, "./modFrete")
        self.descricao_modo_de_frete = ModalidadeFrete.get_descricao(int(self.modo_de_frete)) if self.modo_de_frete else None

        if self.modo_de_frete != ModalidadeFrete.SEM_OCORRENCIA_DE_TRANSPORTE:
            # Volume
            self.quantidade_volumes = extract_value(item, "./vol/qVol")
            self.peso_liquido = extract_value(item, "./vol/pesoL")
            self.peso_bruto = extract_value(item, "./vol/pesoB")

            # Transportadora
            self.cnpj_transportadora = extract_value(item, "./transporta/CNPJ")
            self.nome_transportadora = extract_value(item, "./transporta/xNome")
            self.endereco_transportadora = extract_value(item, "./transporta/xEnder")
            self.municipio_transportadora = extract_value(item, "./transporta/xMun")
            self.uf_transportadora = extract_value(item, "./transporta/UF")
            self.inscricao_estadual_transportadora = extract_value(item, "./transporta/IE")

    def to_dict(self):
        """
        Retorna os atributos da classe em forma de dicionário.

        Returns:
            dict: Dicionário contendo os atributos da classe.
        """
        return self.__dict__
