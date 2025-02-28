from datetime import datetime
import json

def update_controle_importacao(cursor, conn, controle_id, status, descricao_erros=None, dados=None):
    try:
        query = """
            UPDATE controle_importacao
            SET status = %s, descricao_erros = %s, updated_at = %s, dados = %s
            WHERE id = %s
        """
        cursor.execute(
            query,
            (
                status,
                descricao_erros,
                datetime.now(),
                json.dumps(dados) if dados else None,
                controle_id,
            ),
        )
        conn.commit()
    except Exception as ex:
        conn.rollback()
        print(f"Erro ao atualizar controle de importação: {ex}")


def insert_controle_importacao(cursor, conn, nome_arquivo, status, tipo_importacao, cliente, created_by, descricao_erros=None):
    try:
        query = """
            INSERT INTO controle_importacao (
                nome_arquivo, status, tipo_importacao, descricao_erros, cliente, created_by, created_at, updated_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        cursor.execute(
            query,
            (
                nome_arquivo,
                status,
                tipo_importacao,
                descricao_erros,
                cliente,
                created_by,
                datetime.now(),
                datetime.now(),
            ),
        )
        conn.commit()
        return cursor.fetchone()[0]
    except Exception as ex:
        conn.rollback()
        print(f"Erro ao inserir controle de importação: {ex}")
        return None