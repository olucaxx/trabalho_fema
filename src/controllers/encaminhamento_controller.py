from models import encaminhamento_model
from views.encaminhamento import cadastro_encaminhamento_view, tabela_encaminhamentos_view, atualizar_encaminhamento_view

class EncaminhamentoController:
    def __init__(self, root):
        self.root = root
        self.model = encaminhamento_model.Encaminhamento()
        self.view_encaminhamentos = tabela_encaminhamentos_view.TabelaEncaminhamentosView(self.root, self)

    def abrir_tela_cadastro(self):
        self.view_cadastro = cadastro_encaminhamento_view.CadastroEncaminhamentoView(self.root, self)

    def abrir_tela_atualizacao(self):
        selecao = self.view_encaminhamentos.tabela.item(self.view_encaminhamentos.tabela.selection())['values']
        if not selecao:
            return
        self.view_atualizar = atualizar_encaminhamento_view.AtualizarEncaminhamentoView(self.root, self, selecao)

    def cadastrar_encaminhamento(self, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo):
        try:
            self.model.cadastrar(id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo)
            self.view_cadastro.limpar_campos()
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def atualizar_encaminhamento(self, id, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo):
        try:
            self.model.atualizar(id, id_assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo)
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def excluir_encaminhamento(self):
        id = self.view_encaminhamentos.tabela.item(self.view_encaminhamentos.tabela.selection())['values'][0]
        if self.view_encaminhamentos.receber_confirmacao():
            self.model.excluir_encaminhamento_no_bd(id)

    def buscar_encaminhamento(self, nome_escola):
        encaminhamentos = self.model.buscar_encaminhamento_no_bd(nome_escola)
        self.view_encaminhamentos.limpar_tabela()
        for encaminhamento in encaminhamentos:
            self.view_encaminhamentos.exibir_encaminhamento(encaminhamento[0], encaminhamento[1], encaminhamento[2], encaminhamento[3], encaminhamento[4], encaminhamento[5])
