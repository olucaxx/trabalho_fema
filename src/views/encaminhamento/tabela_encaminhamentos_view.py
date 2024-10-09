import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TabelaEncaminhamentosView:
    def __init__(self, master, controller):
        self.master = tk.Toplevel(master)
        self.controller = controller
        self.master.title("Encaminhamentos")
        self.master.resizable(False, False)

        self.frame_botoes = tk.Frame(self.master)
        self.frame_botoes.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        self.frame_botoes.columnconfigure(3, weight=1)

        self.botao_cadastrar = tk.Button(self.frame_botoes, text="Cadastrar", command=self.controller.abrir_tela_cadastro)
        self.botao_cadastrar.grid(row=0, column=0, padx=5)

        self.botao_atualizar = tk.Button(self.frame_botoes, text="Atualizar", command=self.controller.abrir_tela_atualizacao)
        self.botao_atualizar.grid(row=0, column=1, padx=5)

        self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command=self.controller.excluir_encaminhamento)
        self.botao_excluir.grid(row=0, column=2, padx=5)

        self.pesquisa = tk.StringVar()

        self.pesquisa_entry = tk.Entry(self.frame_botoes, textvariable=self.pesquisa)
        self.pesquisa_entry.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        self.botao_buscar = tk.Button(self.frame_botoes, text="Buscar", command= lambda: self.controller.buscar_encaminhamento(self.pesquisa.get()))
        self.botao_buscar.grid(row=0, column=4, padx=5)

        self.tabela = ttk.Treeview(self.master, columns=('id', 'assistente_social', 'instituicoes', 'aluno_matricula', 'data_encaminhamento', 'motivo'), show='headings')
        self.tabela.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

        self.tabela.heading('id', text='ID', anchor='w')
        self.tabela.heading('assistente_social', text='Assistente Social', anchor='w')
        self.tabela.heading('instituicoes', text='Instituições', anchor='w')
        self.tabela.heading('aluno_matricula', text='Matricula', anchor='w')
        self.tabela.heading('data_encaminhamento', text='Data', anchor='w')
        self.tabela.heading('motivo', text='Motivo', anchor='w')

        self.tabela.column('id', width=50, anchor='w')
        self.tabela.column('assistente_social', width=200, anchor='w') 
        self.tabela.column('instituicoes', width=150, anchor='w')
        self.tabela.column('aluno_matricula', width=200, anchor='w')
        self.tabela.column('data_encaminhamento', width=50, anchor='w')
        self.tabela.column('motivo', width=200, anchor='w')

    def limpar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)

    def exibir_encaminhamento(self, id, id_assistente_social, id_instituicoes, aluno_matricula, data_encaminhamento, motivo):
        self.tabela.insert('', 'end', values=(id, id_assistente_social, id_instituicoes, aluno_matricula, data_encaminhamento, motivo))

    def receber_confirmacao(self):
        return messagebox.askyesno("EXCLUSÃO", "Você deseja excluir o encaminhamento?\nEssa ação não pode ser revertida.")
