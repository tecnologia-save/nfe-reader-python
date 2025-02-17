

class ProdutosSave:
    def __init__(self,insert_into_db_by_dict, nota_fiscal_dict ):
        self.insert_into_db_by_dict = insert_into_db_by_dict
        self.produtos_list = None
        if 'produtos' in nota_fiscal_dict:
            self.produtos_list = nota_fiscal_dict['produtos']


    def save_produtos(self, id_nota_fiscal):

        numero_item = 0
        for produto in self.produtos_list:
            numero_item += 1
            produto['nota_fiscal'] = id_nota_fiscal
            id_produto = self.insert_into_db_by_dict('produto_item', produto)
            self.save_impostos(produto['imposto'], id_produto, id_nota_fiscal)
            self.save_item(id_produto, id_nota_fiscal, produto['imposto']['valor_total_tributos'], numero_item)

    def save_item(self, id_produto, id_nota_fiscal, valor_total_tributos, numero_item):
        item = {
            "numero_item": numero_item,
            "valor_total_tributos": valor_total_tributos,
            "produto": id_produto,
            "nota_fiscal": id_nota_fiscal
        }
        self.insert_into_db_by_dict('itens_nota_fiscal ', item)

    def save_impostos(self, impostos, id_produto, id_nota_fiscal):

        if 'cofins' in impostos:
            cofins_produto = impostos['cofins']
            cofins_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('cofins_produto ', cofins_produto)

        if 'pis' in impostos:
            pis_produto = impostos['pis']
            pis_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('pis_produto', pis_produto)

        if 'issqn' in impostos:
            issqn_produto = impostos['issqn']
            issqn_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('issqn_produto ', issqn_produto)


        if 'cofinsst' in impostos:
            cofinsst_produto = impostos['cofinsst']
            cofinsst_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('cofins_st_produto ', cofinsst_produto)

        if 'icms' in impostos:
            icms_produto = impostos['icms']
            icms_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('icms_produto ', icms_produto)

        if 'ipi' in impostos:
            ipi_produto = impostos['ipi']
            ipi_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('ipi_produto ', ipi_produto)

        if 'ii' in impostos:
            imposto_importacao_produto = impostos['ii']
            imposto_importacao_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('imposto_importacao_produto ', imposto_importacao_produto)

        if 'impostodevol' in impostos:
            imposto_devolucao_produto = impostos['impostodevol']
            imposto_devolucao_produto.update(dict(produto= id_produto, nota_fiscal= id_nota_fiscal))
            self.insert_into_db_by_dict('imposto_devolucao_produto ', imposto_devolucao_produto)
