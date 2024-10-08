import sqlite3

class FamiliaMigrations:
    def __init__(self):
        self.conn = sqlite3.connect("banco_de_dados.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS familia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                endereco TEXT NOT NULL,
                celular TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def inserir_familia(self, descricao, endereco, celular):
        self.cursor.execute('''
            INSERT INTO familia (descricao, endereco, celular) 
            VALUES (?, ?, ?);
        ''', (descricao, endereco, celular))
        self.conn.commit()

    def buscar_familia(self, descricao):
        if not descricao:
            self.cursor.execute("SELECT * FROM familia")
            return self.cursor.fetchall()

        self.cursor.execute('''
            SELECT * FROM familia WHERE descricao LIKE ?;
        ''', ('%' + descricao + '%',))
        return self.cursor.fetchall()

    def atualizar_familia(self, familia_id, descricao, endereco, celular):
        self.cursor.execute('''
            UPDATE familia 
            SET descricao = ?, endereco = ?, celular = ? 
            WHERE id = ?;
        ''', (descricao, endereco, celular, familia_id))
        self.conn.commit()

    def deletar_familia(self, familia_id):
        self.cursor.execute('''
            DELETE FROM familia WHERE id = ?;
        ''', (familia_id,))
        self.conn.commit()

    def fechar(self):
        self.conn.close()