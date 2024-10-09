from models import assistente_social_model
from views.assistente_social import selecionar_assistente_view, cadastro_assistente_view, atualizar_assistente_view

class SelecionarAssistenteSocialController:
    def __init__(self, root, encaminhamento_controller):
        self.root = root
        self.model = assistente_social_model.AssistenteSocial()
        self.encaminhamento_controller = encaminhamento_controller
        self.view_assistentes = selecionar_assistente_view.TabelaAssistentesView(self.root, self)

    def abrir_tela_cadastro(self):
        self.view_cadastro = cadastro_assistente_view.CadastroAssistenteView(self.root, self)

    def abrir_tela_atualizacao(self):
        selecao = self.view_assistentes.tabela.item(self.view_assistentes.tabela.selection())['values']
        if not selecao:
            return
        self.view_atualizar = atualizar_assistente_view.AtualizarAssistenteView(self.root, self, selecao)

    def cadastrar_assistente_social(self, nome, celular):
        try:
            self.model.cadastrar(nome, celular)
            self.view_cadastro.limpar_campos()
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def atualizar_assistente_social(self, id_assistente_social, nome, celular):
        try:
            self.model.atualizar(id_assistente_social, nome, celular)
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def excluir_assistente_social(self):
        id = self.view_assistentes.tabela.item(self.view_assistentes.tabela.selection())['values'][0]
        if self.view_assistentes.receber_confirmacao():
            self.model.excluir_assistente_social_no_bd(id)

    def buscar_assistente_social(self, descricao):
        assistentes = self.model.buscar_assistente_social_no_bd(descricao)
        self.view_assistentes.limpar_tabela()
        for assistente in assistentes:
            self.view_assistentes.exibir_assistente_social(assistente[0], assistente[1], assistente[2])

    def selecionar_assistente(self):
        self.encaminhamento_controller.atualizar_id_assistente(self.view_assistentes.tabela.item(self.view_assistentes.tabela.selection())['values'][0])