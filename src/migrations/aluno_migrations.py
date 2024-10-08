import sqlite3

class AlunoMigrations:
    def __init__(self):
        self.conn = sqlite3.connect("banco_de_dados.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS aluno (
                matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                id_escola INTEGER,
                id_familia INTEGER,
                nome TEXT NOT NULL,
                data_nasc TEXT NOT NULL,
                endereco TEXT NOT NULL,
                responsavel TEXT NOT NULL,
                FOREIGN KEY (id_escola) REFERENCES escola(id),
                FOREIGN KEY (id_familia) REFERENCES familia(id)
            );
        ''')
        self.conn.commit()

    def inserir_aluno(self, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        self.cursor.execute('''
            INSERT INTO aluno (id_escola, id_familia, nome, data_nasc, endereco, responsavel) 
            VALUES (?, ?, ?, ?, ?, ?);
        ''', (id_escola, id_familia, nome, data_nasc, endereco, responsavel))
        self.conn.commit()

    def buscar_aluno(self, nome):
        if not nome:
            self.cursor.execute("SELECT * FROM aluno")
            return self.cursor.fetchall()

        self.cursor.execute('''
            SELECT * FROM aluno WHERE nome LIKE ?;
        ''', ('%' + nome + '%',))
        return self.cursor.fetchall()

    def atualizar_aluno(self, matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        self.cursor.execute('''
            UPDATE aluno 
            SET id_escola = ?, id_familia = ?, nome = ?, data_nasc = ?, endereco = ?, responsavel = ?
            WHERE matricula = ?;
        ''', (id_escola, id_familia, nome, data_nasc, endereco, responsavel, matricula))
        self.conn.commit()

    def deletar_aluno(self, matricula):
        self.cursor.execute('''
            DELETE FROM aluno WHERE matricula = ?;
        ''', (matricula,))
        self.conn.commit()

    def fechar(self):
        self.conn.close()