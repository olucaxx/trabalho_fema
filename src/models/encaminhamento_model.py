from migrations import encaminhamento_migrations

class Encaminhamento:
    def __init__(self):
        self.id= None
        self.id_assistente_social= None
        self.instituicoes= None
        self.aluno_matricula= None
        self.data_encaminhamento= None
        self.motivo= None

    def cadastrar(self, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo):
        if not id_assistente_social or not instituicoes or not aluno_matricula or not data_encaminhamento or not motivo:
            raise ValueError("Preencha todos os campos")
        
        self.id_assistente_social= id_assistente_social
        self.instituicoes= instituicoes
        self.aluno_matricula= aluno_matricula
        self.data_encaminhamento= data_encaminhamento
        self.motivo= motivo

        self.cadastrar_no_bd()

    def atualizar(self, id, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo):
        if not id or not id_assistente_social or not instituicoes or not aluno_matricula or not data_encaminhamento or not motivo:
            raise ValueError("Preencha todos os campos")
        self.id= id
        self.id_assistente_social= id_assistente_social
        self.instituicoes= instituicoes
        self.aluno_matricula= aluno_matricula
        self.data_encaminhamento= data_encaminhamento
        self.motivo= motivo

        self.atualizar_no_bd()

    def cadastrar_no_bd(self):
        db = encaminhamento_migrations.EncaminhamentoMigrations()
        db.inserir_encaminhamento(self.id_assistente_social, self.instituicoes, self.aluno_matricula, self.data_encaminhamento, self.motivo)
        db.fechar()

    def atualizar_no_bd(self):
        db = encaminhamento_migrations.EncaminhamentoMigrations()
        db.atualizar_encaminhamento(self.id, self.id_assistente_social, self.instituicoes, self.aluno_matricula, self.data_encaminhamento, self.motivo)
        db.fechar()

    def excluir_encaminhamento_no_bd(self, id):
        db = encaminhamento_migrations.EncaminhamentoMigrations()
        db.deletar_encaminhamento(id)
        db.fechar()

    def buscar_encaminhamento_no_bd(self, nome_escola):
        db = encaminhamento_migrations.EncaminhamentoMigrations()
        encaminhamentos = db.buscar_encaminhamento(nome_escola)
        db.fechar()
        return encaminhamentos
    
