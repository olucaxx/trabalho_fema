from migrations import aluno_migrations

class Aluno:
    def __init__(self):
        self.matricula = None
        self.id_escola = None
        self.id_familia = None
        self.nome = None
        self.data_nasc = None
        self.endereco = None
        self.responsavel = None

    def cadastrar(self, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        if not id_escola or not id_familia or not nome or not data_nasc or not endereco or not responsavel:
            raise ValueError("Preencha todos os campos")
        
        self.id_escola = id_escola
        self.id_familia = id_familia
        self.nome = nome
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.responsavel = responsavel

        self.cadastrar_no_bd()

    def atualizar(self, matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        if not matricula or not id_escola or not id_familia or not nome or not data_nasc or not endereco or not responsavel:
            raise ValueError("Preencha todos os campos")
        
        self.matricula = matricula
        self.id_escola = id_escola
        self.id_familia = id_familia
        self.nome = nome
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.responsavel = responsavel

        self.atualizar_no_bd()

    def cadastrar_no_bd(self):
        db = aluno_migrations.AlunoMigrations()
        db.inserir_aluno(self.id_escola, self.id_familia, self.nome, self.data_nasc, self.endereco, self.responsavel)
        db.fechar()

    def atualizar_no_bd(self):
        db = aluno_migrations.AlunoMigrations()
        db.atualizar_aluno(self.matricula, self.id_escola, self.id_familia, self.nome, self.data_nasc, self.endereco, self.responsavel)
        db.fechar()

    def excluir_escola_no_bd(self, id):
        db = aluno_migrations.AlunoMigrations()
        db.deletar_aluno(id)
        db.fechar()

    def buscar_escola_no_bd(self, nome_escola):
        db = aluno_migrations.AlunoMigrations()
        alunos = db.buscar_aluno(nome_escola)
        db.fechar()
        return alunos
    
