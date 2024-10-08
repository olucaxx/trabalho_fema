import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TabelaAlunosView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Alunos")

        self.frame_botoes = tk.Frame(master)
        self.frame_botoes.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.controller.abrir_tela_cadastro)
        self.botao_cadastrar.grid(row=0, column=0, padx=5)

        self.botao_atualizar = tk.Button(self.frame_botoes, text="Atualizar", command=self.controller.abrir_tela_atualizacao)
        self.botao_atualizar.grid(row=0, column=1, padx=5)

        self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command=self.controller.excluir_aluno)
        self.botao_excluir.grid(row=0, column=2, padx=5)

        self.pesquisa = tk.StringVar()

        self.pesquisa_entry = tk.Entry(self.frame_botoes, textvariable=self.pesquisa)
        self.pesquisa_entry.grid(row=0, column=3, padx=10, pady=10)

        self.botao_buscar = tk.Button(self.frame_botoes, text="Buscar", command= lambda: self.controller.buscar_aluno(self.pesquisa.get()))
        self.botao_buscar.grid(row=0, column=4, padx=5)

        self.tabela = ttk.Treeview(master, columns=('matricula', 'id_escola', 'id_familia', 'nome', 'data_nasc', 'endereco', 'responsavel'), show='headings')
        self.tabela.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        self.tabela.heading('matricula', text='Matricula', anchor='w')
        self.tabela.heading('id_escola', text='ID Escola', anchor='w')
        self.tabela.heading('id_familia', text='ID Família', anchor='w')
        self.tabela.heading('nome', text='Nome', anchor='w')
        self.tabela.heading('data_nasc', text='Data Nasc', anchor='w')
        self.tabela.heading('endereco', text='Endereço', anchor='w')
        self.tabela.heading('responsavel', text='Responsável', anchor='w')

        self.tabela.column('matricula', width=70, anchor='w')
        self.tabela.column('id_escola', width=70, anchor='w') 
        self.tabela.column('id_familia', width=70, anchor='w')
        self.tabela.column('nome', width=200, anchor='w')
        self.tabela.column('data_nasc', width=100, anchor='w')
        self.tabela.column('endereco', width=200, anchor='w')
        self.tabela.column('responsavel', width=100, anchor='w')

    def limpar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

    def exibir_aluno(self, matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel):
        self.tabela.insert('', 'end', values=(matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel))

    def receber_confirmacao(self):
        return messagebox.askyesno("EXCLUSÃO", "Você deseja excluir o aluno?\nEssa ação não pode ser revertida.")
