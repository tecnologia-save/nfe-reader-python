from process.mapping.ResponsavelTecnico.InformacoesResponsavelTecnico import InformacoesResponsavelTecnico


class ResponsavelTecnicoHandler:
    def __init__(self, root):
        self.root = root

    def process(self):
        informacoes_resp_tecnico_tree = self.root.xpath(".//infRespTec")
        if informacoes_resp_tecnico_tree:
            informacoes_resp_tecnico = InformacoesResponsavelTecnico(informacoes_resp_tecnico_tree[0])
            return {"informacoes_resp_tecnico": informacoes_resp_tecnico.to_dict()}
        return {}