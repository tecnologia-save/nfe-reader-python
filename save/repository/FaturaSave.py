

class FaturaSave:
    def __init__(self,insert_into_db_by_dict, nota_fiscal_dict):
        self.insert_into_db_by_dict = insert_into_db_by_dict
        self.fatura_dict = None
        if 'fatura' in nota_fiscal_dict:
            self.fatura_dict = nota_fiscal_dict['fatura']


    def save_fatura(self, id_nota_fiscal):

        if self.fatura_dict is None:
            return

        self.fatura_dict.update({"nota_fiscal": id_nota_fiscal})
        id_fatura = self.insert_into_db_by_dict('fatura_nfe', self.fatura_dict)
        self.save_duplicata(id_nota_fiscal, id_fatura)

    def save_duplicata(self, id_nota_fiscal, id_fatura):
        
        if 'duplicatas' in self.fatura_dict:
            for duplicata in self.fatura_dict['duplicatas']:
                
                duplicata.update({
                    'fatura_nfe': id_fatura,
                    'nota_fiscal': id_nota_fiscal
                })
                self.insert_into_db_by_dict('duplicatas_fatura', duplicata)