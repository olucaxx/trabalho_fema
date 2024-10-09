from models import aluno_model
from views.aluno import selecionar_aluno_view, cadastro_aluno_view, atualizar_aluno_view
from controllers.selecionar_escola_controller import SelecionarEscolaController
from controllers.selecionar_familia_controller import SelecionarFamiliaController

class SelecionarAlunoController:
    def __init__(self, root, encaminhamento_controller):
        self.root = root
        self.model = aluno_model.Aluno()
        self.encaminhamento_controller = encaminhamento_controller
        self.view_alunos = selecionar_aluno_view.TabelaAlunosView(self.root, self)

    def abrir_tela_cadastro(self):
        self.view_cadastro = cadastro_aluno_view.CadastroAlunoView(self.root, self)

    def abrir_tela_atualizacao(self):
        selecao = self.view_alunos.tabela.item(self.view_alunos.tabela.selection())['values']
        if not selecao:
            return
        self.view_atualizar = atualizar_aluno_view.AtualizarAlunoView(self.root, self, selecao)

    def cadastrar_aluno(self, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        try:
            self.model.cadastrar(id_escola, id_familia, nome, data_nasc, endereco, responsavel)
            self.view_cadastro.limpar_campos()
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def atualizar_aluno(self, matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        try:
            self.model.atualizar(matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel)
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def excluir_aluno(self):
        id = self.view_alunos.tabela.item(self.view_alunos.tabela.selection())['values'][0]
        if self.view_alunos.receber_confirmacao():
            self.model.excluir_escola_no_bd(id)

    def buscar_aluno(self, nome_escola):
        alunos = self.model.buscar_escola_no_bd(nome_escola)
        self.view_alunos.limpar_tabela()
        for aluno in alunos:
            self.view_alunos.exibir_aluno(aluno[0], aluno[1], aluno[2], aluno[3], aluno[4], aluno[5], aluno[6])

    def atualizar_id_escola(self, id_escola):
        self.view_cadastro.id_escola.set(id_escola)

    def selecionar_escola(self):
        SelecionarEscolaController(self.root, self)

    def atualizar_id_familia(self, id_familia):
        self.view_cadastro.id_familia.set(id_familia)

    def selecionar_familia(self):
        SelecionarFamiliaController(self.root, self)

    def selecionar_aluno(self):
        self.encaminhamento_controller.atualizar_aluno_matricula(self.view_alunos.tabela.item(self.view_alunos.tabela.selection())['values'][0])