

class TotaisSave:
    def __init__(self,insert_into_db_by_dict, nota_fiscal_dict):
        self.insert_into_db_by_dict = insert_into_db_by_dict
        self.totais_dict = None
        if 'totais' in nota_fiscal_dict:
            self.totais_dict = nota_fiscal_dict['totais']


    def save_totais(self, id_nota_fiscal):

        if 'total_icmstot' in self.totais_dict:
            total_icmstot = self.totais_dict['total_icmstot']
            total_icmstot.update({"nota_fiscal": id_nota_fiscal})
            self.insert_into_db_by_dict('total_icms', total_icmstot)

        if 'total_issqn' in self.totais_dict:
            total_issqn = self.totais_dict['total_issqn']
            total_issqn.update({"nota_fiscal": id_nota_fiscal})
            self.insert_into_db_by_dict('total_issq', total_issqn)

        if 'total_rettrib' in self.totais_dict:
            total_rettrib = self.totais_dict['total_rettrib']
            total_rettrib.update({"nota_fiscal": id_nota_fiscal})
            self.insert_into_db_by_dict('total_retencao_tributos_federais', total_rettrib)
