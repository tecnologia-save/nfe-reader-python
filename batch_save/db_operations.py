import psycopg2
from psycopg2.extras import execute_values

class DB():

    def __init__(self):

        self.conn = psycopg2.connect(
            host='localhost',
            dbname='recuperatax_db',
            user='recuperatax_user',
            password='password'
        )


    def save_all(self, list_to_be_inserted, table_name, returning_values=None):
        if not list_to_be_inserted:
            return []

        listnfs = [self.clear_just_for_text_items(item) for item in list_to_be_inserted]

        try:

            with self.conn.cursor() as cur:
                # Define as colunas a serem inseridas com base nas chaves do primeiro dicionário
                colunas = list(listnfs[0].keys())
                col_names = ', '.join([f'"{col}"' for col in colunas])

                if returning_values:
                    query = f"""
                        INSERT INTO {table_name} ({col_names})
                        VALUES %s
                        RETURNING {returning_values};
                    """
                else:
                    query = f"""
                        INSERT INTO {table_name} ({col_names})
                        VALUES %s
                    """

                valores = [tuple(nota[col] for col in colunas) for nota in listnfs]
                registros = execute_values(cur, query, valores, page_size=1000, fetch=returning_values is not None)
                self.conn.commit()

                return registros

        except Exception as e:
            self.conn.rollback()
            print("Erro ao inserir:", e)
            raise

    def clear_just_for_text_items(self, item: dict):

        if not isinstance(item, dict):
            print(type(item))
            raise Exception("clear_just_for_text_items Data must be dict")

        new_dict = {}
        for value in item:
            if isinstance(item[value], dict) or isinstance(item[value], list):
                continue

            new_dict.update({value: item[value]})

        return new_dict

