from migrations import familia_migrations

class Familia:
    def __init__(self):
        self.id_familia = None 
        self.descricao = None 
        self.endereco = None 
        self.celular = None

    def cadastrar(self, descricao, endereco, celular):
        if not descricao or not endereco or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.descricao = descricao
        self.endereco = endereco
        self.celular = celular

        self.cadastrar_no_bd()

    def atualizar(self, id_familia, descricao, endereco, celular):
        if not descricao or not endereco or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.id_familia = id_familia
        self.descricao = descricao
        self.endereco = endereco
        self.celular = celular

        self.atualizar_no_bd()

    def cadastrar_no_bd(self):
        db = familia_migrations.FamiliaMigrations()
        db.inserir_familia(self.descricao, self.endereco, self.celular)
        db.fechar()

    def atualizar_no_bd(self):
        db = familia_migrations.FamiliaMigrations()
        db.atualizar_familia(self.id_familia, self.descricao, self.endereco, self.celular)
        db.fechar()

    def excluir_familia_no_bd(self, id):
        db = familia_migrations.FamiliaMigrations()
        db.deletar_familia(id)
        db.fechar()

    def buscar_familia_no_bd(self, descricao):
        db = familia_migrations.FamiliaMigrations()
        familias = db.buscar_familia(descricao)
        db.fechar()
        return familias