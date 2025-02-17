
class InfoResponsavelTecnicoSave:
    def __init__(self,insert_into_db_by_dict, nota_fiscal_dict):
        self.insert_into_db_by_dict = insert_into_db_by_dict

        self.informacoes_resp_tecnico_dict = None
        if 'informacoes_resp_tecnico' in nota_fiscal_dict:
            self.informacoes_resp_tecnico_dict = nota_fiscal_dict['informacoes_resp_tecnico']


    def save_info_responsavel_tecnico(self, id_nota_fiscal):

        if self.informacoes_resp_tecnico_dict is None:
            return

        self.informacoes_resp_tecnico_dict.update({"nota_fiscal": id_nota_fiscal})
        self.insert_into_db_by_dict('informacoes_responsavel_tecnico_nfe', self.informacoes_resp_tecnico_dict)
