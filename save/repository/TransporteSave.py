

class TransporteSave:
    def __init__(self,insert_into_db_by_dict, nota_fiscal_dict):
        self.insert_into_db_by_dict = insert_into_db_by_dict
        self.transporte_dict = None

        if 'transp' in nota_fiscal_dict:
            self.transporte_dict = nota_fiscal_dict['transp']


    def save_transporte(self, id_nota_fiscal):

        if self.transporte_dict is None:
            return

        self.transporte_dict.update({"nota_fiscal": id_nota_fiscal})
        self.insert_into_db_by_dict('transporte_nfe', self.transporte_dict)
