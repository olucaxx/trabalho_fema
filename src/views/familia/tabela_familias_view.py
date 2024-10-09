import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TabelaFamiliasView:
    def __init__(self, master, controller):
        self.master = tk.Toplevel(master)
        self.controller = controller
        self.master.title("Familias")
        self.master.resizable(False, False)

        self.frame_botoes = tk.Frame(self.master)
        self.frame_botoes.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.frame_botoes.columnconfigure(3, weight=1)

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.controller.abrir_tela_cadastro)
        self.botao_cadastrar.grid(row=0, column=0, padx=5)

        self.botao_atualizar = tk.Button(self.frame_botoes, text="Atualizar", command=self.controller.abrir_tela_atualizacao)
        self.botao_atualizar.grid(row=0, column=1, padx=5)

        self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command=self.controller.excluir_familia)
        self.botao_excluir.grid(row=0, column=2, padx=5)

        self.pesquisa = tk.StringVar()

        self.pesquisa_entry = tk.Entry(self.frame_botoes, textvariable=self.pesquisa)
        self.pesquisa_entry.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.botao_buscar = tk.Button(self.frame_botoes, text="Buscar", command= lambda: self.controller.buscar_familia(self.pesquisa.get()))
        self.botao_buscar.grid(row=0, column=4, padx=5)

        self.tabela = ttk.Treeview(self.master, columns=('id', 'descricao', 'endereco', 'celular'), show='headings')
        self.tabela.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        self.tabela.heading('id', text='ID', anchor='w')
        self.tabela.heading('descricao', text='Diretor', anchor='w')
        self.tabela.heading('endereco', text='Endereço', anchor='w')
        self.tabela.heading('celular', text='Celular', anchor='w')

        self.tabela.column('id', width=50, anchor='w')
        self.tabela.column('descricao', width=150, anchor='w')
        self.tabela.column('endereco', width=200, anchor='w')
        self.tabela.column('celular', width=100, anchor='w')

    def limpar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

    def exibir_familia(self, id, descricao, endereco, celular):
        self.tabela.insert('', 'end', values=(id, descricao, endereco, celular))

    def receber_confirmacao(self):
        return messagebox.askyesno("EXCLUSÃO", "Você deseja excluir a familia?\nEssa ação não pode ser revertida.")
