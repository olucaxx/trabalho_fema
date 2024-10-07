import sqlite3

class EscolaMigrations:
    def __init__(self):
        self.conn = sqlite3.connect("banco_de_dados.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS escola (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                diretor TEXT NOT NULL,
                endereco TEXT NOT NULL,
                celular TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def inserir_escola(self, nome, diretor, endereco, celular):
        self.cursor.execute('''
            INSERT INTO escola (nome, diretor, endereco, celular) 
            VALUES (?, ?, ?, ?);
        ''', (nome, diretor, endereco, celular))
        self.conn.commit()

    def buscar_escola(self, nome_escola):
        if not nome_escola:
            self.cursor.execute("SELECT * FROM escola")
            return self.cursor.fetchall()

        self.cursor.execute('''
            SELECT * FROM escola WHERE nome LIKE ?;
        ''', ('%' + nome_escola + '%',))
        return self.cursor.fetchall()

    def atualizar_escola(self, escola_id, nome, diretor, endereco, celular):
        self.cursor.execute('''
            UPDATE escola 
            SET nome = ?, diretor = ?, endereco = ?, celular = ? 
            WHERE id = ?;
        ''', (nome, diretor, endereco, celular, escola_id))
        self.conn.commit()

    def deletar_escola(self, escola_id):
        self.cursor.execute('''
            DELETE FROM escola WHERE id = ?;
        ''', (escola_id,))
        self.conn.commit()

    def fechar(self):
        self.conn.close()