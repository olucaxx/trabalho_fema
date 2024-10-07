from migrations import escola_migrations

class Escola:
    def __init__(self):
        self.id_escola = None
        self.nome_escola = None
        self.serie = None
        self.diretor = None
        self.endereco = None
        self.celular = None

    def cadastrar(self, nome_escola, serie, diretor, endereco, celular):
        if not nome_escola or not serie or not diretor or not endereco or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.nome_escola = nome_escola
        self.serie = serie
        self.diretor = diretor
        self.endereco = endereco
        self.celular = celular

        self.cadastrar_no_bd()

    def atualizar(self, id_escola, nome_escola, serie, diretor, endereco, celular):
        if not nome_escola or not serie or not diretor or not endereco or not celular:
            raise ValueError("Preencha todos os campos")
        
        self.id_escola = id_escola
        self.nome_escola = nome_escola
        self.serie = serie
        self.diretor = diretor
        self.endereco = endereco
        self.celular = celular

        self.atualizar_no_bd()

    def cadastrar_no_bd(self):
        db = escola_migrations.EscolaMigrations()
        db.inserir_escola(self.nome_escola, self.serie, self.diretor, self.endereco, self.celular)
        db.fechar()

    def atualizar_no_bd(self):
        db = escola_migrations.EscolaMigrations()
        db.atualizar_escola(self.id_escola, self.nome_escola, self.serie, self.diretor, self.endereco, self.celular)
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

    def set_nome_escola(self, value):
        if not value or len(value) < 3:
            raise ValueError("O nome da escola deve ter pelo menos 3 caracteres.")
        self.nome_escola = value

    def get_nome_escola(self):
        return self.nome_escola

    def set_serie(self, value):
        if not value:
            raise ValueError("A série não pode estar vazia.")
        self.serie = value

    def get_serie(self):
        return self.serie

    def set_diretor(self, value):
        if not value:
            raise ValueError("O nome do direitor não foi informado.")
        self.serie = value

    def get_diretor(self):
        return self.serie

    def set_endereco(self, value):
        if not value or len(value) < 5:
            raise ValueError("O endereço deve ter pelo menos 5 caracteres.")
        self.endereco = value

    def get_endereco(self):
        return self.endereco

    def set_celular(self, value):
        if not value.isdigit() or len(value) < 10:
            raise ValueError("O celular deve conter apenas dígitos e ter pelo menos 10 caracteres.")
        self.celular = value

    def get_celular(self):
        return self.celular
    

