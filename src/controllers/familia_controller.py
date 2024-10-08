from models import familia_model
from views.familia import tabela_familias_view, atualizar_familia_view, cadastro_familia_view

class FamiliaController:
    def __init__(self, root):
        self.root = root
        self.model = familia_model.Familia()
        self.view_familias = tabela_familias_view.TabelaFamiliasView(self.root, self)

    def abrir_tela_cadastro(self):
        self.view_cadastro = cadastro_familia_view.CadastroFamiliaView(self.root, self)

    def abrir_tela_atualizacao(self):
        selecao = self.view_familias.tabela.item(self.view_familias.tabela.selection())['values']
        if not selecao:
            return
        self.view_atualizar = atualizar_familia_view.AtualizarFamiliaView(self.root, self, selecao)

    def cadastrar_familia(self, descricao, endereco, celular):
        try:
            self.model.cadastrar(descricao, endereco, celular)
            self.view_cadastro.limpar_campos()
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def atualizar_familia(self, id_familia, descricao, endereco, celular):
        try:
            self.model.atualizar(id_familia, descricao, endereco, celular)
        except ValueError as e:
            self.view_cadastro.mostrar_alerta(e)

    def excluir_familia(self):
        id = self.view_familias.tabela.item(self.view_familias.tabela.selection())['values'][0]
        if self.view_familias.receber_confirmacao():
            self.model.excluir_familia_no_bd(id)

    def buscar_familia(self, descricao):
        familias = self.model.buscar_familia_no_bd(descricao)
        self.view_familias.limpar_tabela()
        for familia in familias:
            self.view_familias.exibir_familia(familia[0], familia[1], familia[2], familia[3])