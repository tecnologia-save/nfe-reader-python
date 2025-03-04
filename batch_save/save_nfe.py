from datetime import datetime
from batch_save.db_operations import DB
import copy
from pprint import pprint

def save_dicts(notas_fiscais_originais):




    listnfs = copy.deepcopy(notas_fiscais_originais)

    if not listnfs:
        return []

    for nota_fiscal in listnfs:
        insert_fict_values(nota_fiscal)


    with DB() as db:
        returning_values = db.save_all(listnfs, 'nota_fiscal', 'id, chave')
        notas = concact_generated_ids(copy.deepcopy(notas_fiscais_originais), returning_values, 'nota_fiscal', 'chave', 0, 1)

        produtos_to_insert = []
        for nota in notas:
            if 'produtos' in nota:
                for produto in nota['produtos']:
                    produto['nota_fiscal'] = nota['nota_fiscal']
                    insert_fict_values2(produto)
                    produtos_to_insert.append(produto)

        returning_values = db.save_all(produtos_to_insert, 'produto_item', 'id, codigo_produto')


        tables_to_insert = {}

        for produto in produtos_to_insert:
            if 'imposto' in produto:
                for key, value in produto['imposto'].items():

                    if value is None:
                        continue

                    value['codigo_produto'] = produto['codigo_produto']
                    value['nota_fiscal'] = produto['nota_fiscal']
                    value = concact_generated_ids([value], returning_values, 'produto', 'codigo_produto', 0, 1)[0]
                    insert_fict_values2(value)
                    value.pop('codigo_produto')
                    
                    if key not in tables_to_insert.keys():

                        tables_to_insert.update({key: [value]})
                    else:
                        tables_to_insert[key].append(value)


        for key, value in tables_to_insert.items():
            returning_values = db.save_all(value, key)



        totais_to_insert = {}
        for nota in notas:
            if 'totais' in nota:
                for key, value in nota['totais'].items():
                    value['nota_fiscal'] = nota['nota_fiscal']
                    insert_fict_values2(value)
                    
                    if key not in totais_to_insert.keys():

                        totais_to_insert.update({key: [value]})
                    else:
                        totais_to_insert[key].append(value)

        for key, value in totais_to_insert.items():
            returning_values = db.save_all(value, key)


        faturas_to_insert = []
        for nota in notas:
            if 'fatura' in nota:
                nota['fatura']['nota_fiscal'] = nota['nota_fiscal']
                insert_fict_values2(nota['fatura'])
                faturas_to_insert.append(nota['fatura'])

        
        returning_values = db.save_all(faturas_to_insert, 'fatura_nfe', 'id, numero_fatura')
        faturas = concact_generated_ids(faturas_to_insert, returning_values, 'id', 'numero_fatura', 0, 1)
        duplicatas_to_insert = []
        for fatura in faturas:
            if 'duplicatas' in fatura:
                for duplicata in fatura['duplicatas']:
                    duplicata['nota_fiscal'] = fatura['nota_fiscal']
                    duplicata['fatura_nfe'] = fatura['id']
                    insert_fict_values2(duplicata)
                    duplicatas_to_insert.append(duplicata)

        returning_values = db.save_all(duplicatas_to_insert, 'duplicatas_fatura')

        responsavel_tecnico_to_insert = []
        for nota in notas:
            if 'informacoes_resp_tecnico' in nota:
                nota['informacoes_resp_tecnico']['nota_fiscal'] = nota['nota_fiscal']
                insert_fict_values2(nota['informacoes_resp_tecnico'])
                responsavel_tecnico_to_insert.append(nota['informacoes_resp_tecnico'])
        

        returning_values = db.save_all(responsavel_tecnico_to_insert, 'informacoes_responsavel_tecnico_nfe')


        transporte_to_insert = []
        for nota in notas:
            if 'transp' in nota:
                nota['transp']['nota_fiscal'] = nota['nota_fiscal']
                insert_fict_values2(nota['transp'])
                transporte_to_insert.append(nota['transp'])

        returning_values = db.save_all(transporte_to_insert, 'transporte_nfe')

    

def concact_generated_ids(lista_notas_fiscais, returned_values, returned_new_id_key, compare_key, returned_id_index, compare_key_index):
    lookup = {value[compare_key_index]: value[returned_id_index] for value in returned_values}
    for nota_fiscal in lista_notas_fiscais:
        chave = nota_fiscal.get(compare_key)
        if chave in lookup:
            nota_fiscal[returned_new_id_key] = lookup[chave]

    return lista_notas_fiscais

def insert_fict_values2(dict):
    dict.update({"created_at": datetime.now()})
    dict.update({"updated_at": datetime.now()})
    dict.update({"cliente": 1})
    dict.update({"created_by": 1})
    
def insert_fict_values(nfe):
    nfe.update({"emitente": 1})
    nfe.update({"created_at": datetime.now()})
    nfe.update({"updated_at": datetime.now()})
    nfe.update({"created_by": 1})
    nfe.update({"cliente": 1})



