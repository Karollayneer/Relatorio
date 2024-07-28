import sqlite3

def conectar():
    return sqlite3.connect('banco_de_dados.db')

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS cx_prob')  # Isso exclui a tabela existente para recriá-la
    cursor.execute('''
    CREATE TABLE cx_prob (
        num_situacao INTEGER NOT NULL,
        num_cx TEXT NOT NULL,
        data TEXT NOT NULL,
        descricao TEXT NOT NULL
    )
    ''')
    conn.commit()

def inserir_dados(conn, num_situacao, num_cx, data, descricao):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO cx_prob (num_situacao, num_cx, data, descricao) VALUES (?, ?, ?, ?)
    ''', (num_situacao, num_cx, data, descricao))
    conn.commit()

def buscar_dados(conn, filtro=""):
    cursor = conn.cursor()
    if filtro:
        cursor.execute('''
        SELECT * FROM cx_prob WHERE num_cx LIKE ? OR descricao LIKE ? OR data LIKE ? OR num_situacao LIKE ?
        ''', (f'%{filtro}%', f'%{filtro}%', f'%{filtro}%', f'%{filtro}%'))
    else:
        cursor.execute('SELECT * FROM cx_prob')
    return cursor.fetchall()

if __name__ == "__main__":
    conn = conectar()
    criar_tabela(conn)
    inserir_dados(conn, 1, 'I12018', '15/10/2024', 'Caixa com processo sem estar na lista')
    inserir_dados(conn, 2, 'P25018', '10/12/2024', 'Caixa sem lista de processo')
    dados = buscar_dados(conn)
    for dado in dados:
        print(dado)
    conn.close()
