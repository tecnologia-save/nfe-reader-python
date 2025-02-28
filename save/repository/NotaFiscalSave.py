class NotaFiscalSave:
    def __init__(self, nota_fiscal_dict, cursor, cliente):
        self.nota_fiscal_dict = nota_fiscal_dict
        self.cursor = cursor
        self.cliente = cliente




    def save_nota_fiscal(self, insert_into_db_by_dict, id_emitente, id_destinatario, controler_importacao):
        if id_emitente is None:
            raise Exception("ID do emitente não encontrado")

        self.nota_fiscal_dict['emitente'] = id_emitente
        self.nota_fiscal_dict['destinatario'] = id_destinatario
        self.nota_fiscal_dict['controler_importacao'] = controler_importacao

        return insert_into_db_by_dict('nota_fiscal', self.nota_fiscal_dict)

