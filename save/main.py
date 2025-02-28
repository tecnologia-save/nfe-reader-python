from datetime import datetime

import psycopg2
import re
from save.repository.FaturaSave import FaturaSave
from save.repository.InfoResponsavelTecnicoSave import InfoResponsavelTecnicoSave
from save.repository.NotaFiscalSave import NotaFiscalSave
from save.repository.ProdutosSave import ProdutosSave
from save.repository.TotaisSave import TotaisSave
from save.repository.TransporteSave import TransporteSave


class SaveNotaFiscal:
    def __init__(self, nota_fiscal_dict, standard_db_items, controle_importacao_id, conn, cursor):
        self.nota_fiscal_dict = nota_fiscal_dict
        self.standard_db_items = standard_db_items
        self.controle_importacao_id = controle_importacao_id

        self.conn = conn
        self.cursor = cursor

        self.validar_xml()


    def save(self):

        emitente_id = None
        if 'emitente' in self.nota_fiscal_dict:
            emitente_id = self.find_id_in_db('entidade', 'cgc', self.limpa_string_numeros(self.nota_fiscal_dict['emitente']['cgc']), False)
            if not emitente_id:
                emitente_id = self.insert_into_db_by_dict('entidade', self.nota_fiscal_dict['emitente'])

        destinatario_id = None
        if 'destinatario' in self.nota_fiscal_dict and self.nota_fiscal_dict['destinatario']['cgc'] is not None:
            destinatario_id = self.find_id_in_db('entidade', 'cgc', self.limpa_string_numeros(self.nota_fiscal_dict['destinatario']['cgc']), False)
            if not destinatario_id:    
                destinatario_id = self.insert_into_db_by_dict('entidade', self.nota_fiscal_dict['destinatario'])


        nota_fiscal_save = NotaFiscalSave(self.nota_fiscal_dict, self.cursor, self.standard_db_items['cliente'])
        id_nota_fiscal = nota_fiscal_save.save_nota_fiscal(self.insert_into_db_by_dict, emitente_id, destinatario_id, self.controle_importacao_id)

        produtos_save = ProdutosSave(self.insert_into_db_by_dict, self.nota_fiscal_dict)
        produtos_save.save_produtos(id_nota_fiscal)

        totais_save = TotaisSave(self.insert_into_db_by_dict, self.nota_fiscal_dict)
        totais_save.save_totais(id_nota_fiscal)

        fatura_save = FaturaSave(self.insert_into_db_by_dict, self.nota_fiscal_dict)
        fatura_save.save_fatura(id_nota_fiscal)

        info_responsavel_tecnico_save = InfoResponsavelTecnicoSave(self.insert_into_db_by_dict, self.nota_fiscal_dict)
        info_responsavel_tecnico_save.save_info_responsavel_tecnico(id_nota_fiscal)

        transporte_save = TransporteSave(self.insert_into_db_by_dict, self.nota_fiscal_dict)
        transporte_save.save_transporte(id_nota_fiscal)

    def exclude_dict_or_list_items(self, data: dict):
        new_dict = {}
        for key, value in data.items():
            if not (isinstance(value, dict) or isinstance(value, list)):
                new_dict[key] = value
        return new_dict

    def insert_into_db_by_dict(self, table_name: str, data: dict | list):

        if not data:
            return

        elif not isinstance(data, dict):
            raise Exception("insert_into_db_by_dict Data must be dict")

        data = self.exclude_dict_or_list_items(data)
        return self.insert_operations(table_name, data)

    def insert_operations(self, table_name: str, record: dict):
            record.update(self.standard_db_items)
            record.update({"created_at": datetime.now()})
            record.update({"updated_at": datetime.now()})

            keys = ', '.join(f'"{key}"' for key in record.keys())
            placeholders = ', '.join(['%s'] * len(record))
            values = tuple(record.values())

            sql = f"INSERT INTO {table_name} ({keys}) VALUES ({placeholders}) RETURNING id"
            self.cursor.execute(sql, values)
            generated_id = self.cursor.fetchone()[0]

            return generated_id


    def validar_xml(self):
        if not 'emitente' in self.nota_fiscal_dict:
            raise Exception('Emitente não encontrado, Favor validar se é um arquivo XML de NF')

        emitente = self.nota_fiscal_dict['emitente']

        if not 'chave' in self.nota_fiscal_dict:
            raise Exception('Chave da nota fiscal não encontrada. Verifique se o xml é válido')


        chave_ja_existe = self.exists_in_db('nota_fiscal', 'chave', self.nota_fiscal_dict['chave'])

        if chave_ja_existe:
            raise Exception(f"NFE já importada. Chave: {self.nota_fiscal_dict['chave']}")


        cnpj_matriz_ou_filal_emitente = self.busca_cnpj_matriz_ou_filial(emitente, self.standard_db_items['cliente'])


        cnpj_matriz_ou_filal_destinatario = None

        if not cnpj_matriz_ou_filal_emitente and (self.nota_fiscal_dict['modelo_nfe'] == 55 or 'destinatario' in self.nota_fiscal_dict):
            if not 'destinatario' in self.nota_fiscal_dict:
                raise Exception('Destinatário não encontrado em xml do tipo NFe')

            cnpj_matriz_ou_filal_destinatario = self.busca_cnpj_matriz_ou_filial(self.nota_fiscal_dict['destinatario'], self.standard_db_items['cliente'])


        if (not cnpj_matriz_ou_filal_emitente) and (not cnpj_matriz_ou_filal_destinatario):
            if 'destinatario' in self.nota_fiscal_dict:
                cnpj_destinatario = self.nota_fiscal_dict['destinatario']['cgc']
            else:
                cnpj_destinatario = None

            if not cnpj_destinatario:
                raise Exception(f"Nem Emitente CNPJ {emitente['cgc']} nem destinatário cadastrados")

            raise Exception(f"Nem Emitente CNPJ {emitente['cgc']} nem destinatário {cnpj_destinatario} cadastrados")



    def limpa_string_numeros(self, string: str):
        return re.sub(r'\D', '', string)


    def find_id_in_db(self, table_name, key_column, key_value, include_cliente=True):
        if include_cliente:
            sql = f"SELECT id FROM {table_name} WHERE {key_column} = %s AND cliente = {self.standard_db_items['cliente']} AND  deleted_at IS NULL"
        else:
            sql = f"SELECT id FROM {table_name} WHERE {key_column} = %s  AND deleted_at IS NULL"

        self.cursor.execute(sql, (key_value,))
        result =self.cursor.fetchone()

        return result[0] if result else None

    def exists_in_db(self, table_name, key_column, key_value, include_cliente=True):
        """
        Verifica se já existe uma entrada no banco de dados com a mesma chave.
        """

        if include_cliente:
            sql = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE {key_column} = %s AND cliente = {self.standard_db_items['cliente']} AND  deleted_at IS NULL)"
        else:
            sql = f"SELECT EXISTS(SELECT 1 FROM {table_name} WHERE {key_column} = %s  AND deleted_at IS NULL)"

        self.cursor.execute(sql, (key_value,))
        return self.cursor.fetchone()[0]

    def busca_cnpj_matriz_ou_filial(self, entidade_dict, cliente):
        cnpj_entidade = entidade_dict['cgc']

        cnpj_entidade = self.limpa_string_numeros(cnpj_entidade)
        raiz = cnpj_entidade[:8]

        query = "SELECT cnpj, id FROM empresas WHERE cliente = %s AND cnpj ILIKE %s  AND  deleted_at IS NULL LIMIT 1"

        self.cursor.execute(query, (cliente, f"{raiz}%"))
        result = self.cursor.fetchone()

        if result:
            cnpj_empresa_db, id_empresa_db = result
        else:
            raise ValueError(f"Empresa não encontrada para o cliente '{cliente}' com CNPJ raiz '{raiz}' CNPJ '{cnpj_entidade}'.")

        cnpj_empresa_db = self.limpa_string_numeros(cnpj_empresa_db[0])

        # Se o cnpj for diferente do da empresa é porque é filial
        if cnpj_entidade == cnpj_empresa_db:
            return cnpj_empresa_db
        else:
            query = "SELECT cnpj FROM filiais_empresa WHERE cliente = %s AND cnpj = %s  AND  deleted_at IS NULL LIMIT 1"
            self.cursor.execute(query, (cliente, f"{raiz}%"))
            cnpj_filial_db = self.cursor.fetchone()

            if cnpj_filial_db is None:
                self.cadastra_filial_db(entidade_dict, id_empresa_db)
                self.conn.commit()
                return entidade_dict['cgc']
            else:
                return cnpj_filial_db[0]

    def cadastra_filial_db(self, entidade, empresa_id):
        obj = {
            "cnpj": self.limpa_string_numeros(entidade['cgc']),
            "nome": entidade['nome'],
            "empresa": empresa_id,
        }
        return self.insert_into_db_by_dict('filiais_empresa', obj)

