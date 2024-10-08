from models import escola_model
from views.escola import cadastro_escola_view, tabela_escolas_view, atualizar_escola_view

class EscolaController:
    def __init__(self, root):
        self.root = root
        self.model = escola_model.Escola()
        self.view_escolas = tabela_escolas_view.TabelaEscolasView(self.root, self)

    def abrir_tela_cadastro(self):
        self.view_cadastro = cadastro_escola_view.CadastroEscolaView(self.root, self)

    def abrir_tela_atualizacao(self):
        selecao = self.view_escolas.tabela.item(self.view_escolas.tabela.selection())['values']
        if not selecao:
            return
        self.view_atualizar = atualizar_escola_view.AtualizarEscolaView(self.root, self, selecao)

    def cadastrar_escola(self, nome_escola, diretor, endereco, celular):
        try:
            self.model.cadastrar(nome_escola, diretor, endereco, celular)
            self.view_cadastro.limpar_campos()
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def atualizar_escola(self, id_escola, nome_escola, diretor, endereco, celular):
        try:
            self.model.atualizar(id_escola, nome_escola, diretor, endereco, celular)
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def excluir_escola(self):
        id = self.view_escolas.tabela.item(self.view_escolas.tabela.selection())['values'][0]
        if self.view_escolas.receber_confirmacao():
            self.model.excluir_escola_no_bd(id)

    def buscar_escola(self, nome_escola):
        escolas = self.model.buscar_escola_no_bd(nome_escola)
        self.view_escolas.limpar_tabela()
        for escola in escolas:
            self.view_escolas.exibir_escola(escola[0], escola[1], escola[2], escola[3], escola[4])
