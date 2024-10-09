from migrations import assist_social_migrations

class AssistenteSocial:
    def __init__(self):
        self.id_assistente_social = None 
        self.nome = None 
        self.celular = None

    def cadastrar(self, nome, celular):
        if not nome or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.nome = nome
        self.celular = celular

        self.cadastrar_no_bd()

    def atualizar(self, id_assistente_social, nome, celular):
        if not nome or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.id_assistente_social = id_assistente_social
        self.nome = nome
        self.celular = celular

        self.atualizar_no_bd()

    def cadastrar_no_bd(self):
        db = assist_social_migrations.AssistenteSocialMigrations()
        db.inserir_assistente_social(self.nome, self.celular)
        db.fechar()

    def atualizar_no_bd(self):
        db = assist_social_migrations.AssistenteSocialMigrations()
        db.atualizar_assistente_social(self.id_assistente_social, self.nome, self.celular)
        db.fechar()

    def excluir_assistente_social_no_bd(self, id):
        db = assist_social_migrations.AssistenteSocialMigrations()
        db.deletar_assistente_social(id)
        db.fechar()

    def buscar_assistente_social_no_bd(self, nome):
        db = assist_social_migrations.AssistenteSocialMigrations()
        assistentes = db.buscar_assistente_social(nome)
        db.fechar()
        return assistentes