from migrations import escola_migrations

class Escola:
    def __init__(self):
        self.id_escola = None
        self.nome_escola = None
        self.diretor = None
        self.endereco = None
        self.celular = None

    def cadastrar(self, nome_escola, diretor, endereco, celular):
        if not nome_escola or not diretor or not endereco or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.nome_escola = nome_escola
        self.diretor = diretor
        self.endereco = endereco
        self.celular = celular

        self.cadastrar_no_bd()

    def atualizar(self, id_escola, nome_escola, diretor, endereco, celular):
        if not nome_escola or not diretor or not endereco or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.id_escola = id_escola
        self.nome_escola = nome_escola
        self.diretor = diretor
        self.endereco = endereco
        self.celular = celular

        self.atualizar_no_bd()

    def cadastrar_no_bd(self):
        db = escola_migrations.EscolaMigrations()
        db.inserir_escola(self.nome_escola, self.diretor, self.endereco, self.celular)
        db.fechar()

    def atualizar_no_bd(self):
        db = escola_migrations.EscolaMigrations()
        db.atualizar_escola(self.id_escola, self.nome_escola, self.diretor, self.endereco, self.celular)
        db.fechar()

    def excluir_escola_no_bd(self, id):
        db = escola_migrations.EscolaMigrations()
        db.deletar_escola(id)
        db.fechar()

    def buscar_escola_no_bd(self, nome_escola):
        db = escola_migrations.EscolaMigrations()
        escolas = db.buscar_escola(nome_escola)
        db.fechar()
        return escolas
    
