import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TabelaAssistentesView:
    def __init__(self, master, controller):
        self.master = tk.Toplevel(master)
        self.controller = controller
        self.master.title("Assistentes Sociais")
        self.master.resizable(False, False)

        self.frame_botoes = tk.Frame(self.master)
        self.frame_botoes.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.frame_botoes.columnconfigure(3, weight=1)

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.controller.abrir_tela_cadastro)
        self.botao_cadastrar.grid(row=0, column=0, padx=5)

        self.botao_atualizar = tk.Button(self.frame_botoes, text="Atualizar", command=self.controller.abrir_tela_atualizacao)
        self.botao_atualizar.grid(row=0, column=1, padx=5)

        self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command=self.controller.excluir_assistente_social)
        self.botao_excluir.grid(row=0, column=2, padx=5)

        self.pesquisa = tk.StringVar()

        self.pesquisa_entry = tk.Entry(self.frame_botoes, textvariable=self.pesquisa)
        self.pesquisa_entry.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.botao_selecionar = tk.Button(self.frame_botoes, text="Selecionar", command= self.selecionar_assistente)
        self.botao_selecionar.grid(row=0, column=5, padx=5)

        self.botao_buscar = tk.Button(self.frame_botoes, text="Buscar", command= lambda: self.controller.buscar_assistente_social(self.pesquisa.get()))
        self.botao_buscar.grid(row=0, column=4, padx=5)

        self.tabela = ttk.Treeview(self.master, columns=('id', 'nome', 'celular'), show='headings')
        self.tabela.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        self.tabela.heading('id', text='ID', anchor='w')
        self.tabela.heading('nome', text='Nome', anchor='w')
        self.tabela.heading('celular', text='Celular', anchor='w')

        self.tabela.column('id', width=50, anchor='w')
        self.tabela.column('nome', width=200, anchor='w')
        self.tabela.column('celular', width=100, anchor='w')

    def limpar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

    def exibir_assistente_social(self, id, nome, celular):
        self.tabela.insert('', 'end', values=(id, nome, celular))

    def receber_confirmacao(self):
        return messagebox.askyesno("EXCLUSÃO", "Você deseja excluir a assistente social?\nEssa ação não pode ser revertida.")

    def selecionar_assistente(self):
        self.controller.selecionar_assistente()
        self.master.destroy()