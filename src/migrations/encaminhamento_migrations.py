import sqlite3

class EncaminhamentoMigrations:
    def __init__(self):
        self.conn = sqlite3.connect("banco_de_dados.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS encaminhamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_assistente_social INTERGER,
            instituicoes TEXT NOT NULL,
            aluno_matricula INTERGER,
            data_encaminhamento TEXT NOT NULL,
            motivo TEXT NOT NULL,
            FOREIGN KEY (aluno_matricula) REFERENCES aluno(matricula)                                      
            );
        ''')
        self.conn.commit()

    def inserir_encaminhamento(self, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo):
        self.cursor.execute('''
            INSERT INTO encaminhamento (id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo) 
            VALUES (?, ?, ?, ?, ?);
        ''', (id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo))
        self.conn.commit()

    def buscar_encaminhamento(self, aluno_matricula):
        if not aluno_matricula:
            self.cursor.execute("SELECT * FROM encaminhamento")
            return self.cursor.fetchall()

        self.cursor.execute('''
            SELECT * FROM encaminhamento WHERE aluno_matricula LIKE ?;
        ''', ('%' + aluno_matricula + '%',))
        return self.cursor.fetchall()

    def atualizar_encaminhamento(self,id, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo):
        self.cursor.execute('''
            UPDATE encaminhamento 
            SET id_assistente_social = ?, instituicoes = ?, aluno_matricula = ?, data_encaminhamento = ?, motivo = ? 
            WHERE id = ?;
        ''', (id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo, id))
        self.conn.commit()

    def deletar_encaminhamento(self,id ):
        self.cursor.execute('''
            DELETE FROM encaminhamento WHERE id = ?;
        ''', (id,))
        self.conn.commit()

    def fechar(self):
        self.conn.close()