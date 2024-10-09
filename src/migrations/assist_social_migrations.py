import sqlite3

class AssistenteSocialMigrations:
    def __init__(self):
        self.conn = sqlite3.connect("banco_de_dados.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS assistente_social (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                celular TEXT NOT NULL
            );
        ''')
        self.conn.commit()

    def inserir_assistente_social(self, nome, celular):
        self.cursor.execute('''
            INSERT INTO assistente_social (nome, celular) 
            VALUES (?, ?);
        ''', (nome, celular))
        self.conn.commit()

    def buscar_assistente_social(self, nome):
        if not nome:
            self.cursor.execute("SELECT * FROM assistente_social")
            return self.cursor.fetchall()

        self.cursor.execute('''
            SELECT * FROM assistente_social WHERE nome LIKE ?;
        ''', ('%' + nome + '%',))
        return self.cursor.fetchall()

    def atualizar_assistente_social(self, assistente_social_id, nome, celular):
        self.cursor.execute('''
            UPDATE assistente_social 
            SET nome = ?, celular = ?
            WHERE id = ?;
        ''', (nome, celular, assistente_social_id))
        self.conn.commit()

    def deletar_assistente_social(self, assistente_social_id):
        self.cursor.execute('''
            DELETE FROM assistente_social WHERE id = ?;
        ''', (assistente_social_id,))
        self.conn.commit()

    def fechar(self):
        self.conn.close()