import tkinter as tk
from tkinter import messagebox

#   self.tabela.heading('id', text='ID', anchor='w')
 #       self.tabela.heading('assistente_social', text='Assistente Social', anchor='w')
  #      self.tabela.heading('instituicoes', text='Instituições', anchor='w')
   #     self.tabela.heading('aluno_matricula', text='Matricula', anchor='w')
    #    self.tabela.heading('data_encaminhamento', text='Data do encaminhamento', anchor='w')
     #   self.tabela.heading('motivo', text='Motivo', anchor='w')



class CadastroEncaminhamentoView:
    def __init__(self, root, controller):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.master.title("Cadastro Encaminhamento")
        self.master.resizable(False, False)

        self.assistente_social = tk.StringVar()
        self.instituicoes = tk.StringVar() 
        self.aluno_matricula = tk.StringVar()
        self.data_encaminhamento = tk.StringVar()
        self.motivo = tk.StringVar()


        tk.Label(self.master, text="Assistente Social:").grid(row=0, column=0, padx=10, pady=10)
        self.assistente_entry = tk.Entry(self.master, textvariable=self.assistente_social)
        self.assistente_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Instituições:").grid(row=1, column=0, padx=10, pady=10)
        self.instituicoes_entry = tk.Entry(self.master, textvariable=self.instituicoes) 
        self.instituicoes_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Matricula:").grid(row=2, column=0, padx=10, pady=10)
        self.aluno_matricula_entry = tk.Entry(self.master, textvariable=self.aluno_matricula)
        self.aluno_matricula_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Data do encaminhamento:").grid(row=3, column=0, padx=10, pady=10)
        self.data_encaminhamento_entry = tk.Entry(self.master, textvariable=self.data_encaminhamento)
        self.data_encaminhamento_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Motivo:").grid(row=4, column=0, padx=10, pady=10)
        self.motivo_entry = tk.Entry(self.master, textvariable=self.motivo)
        self.motivo_entry.grid(row=4, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.master, text="Cadastrar", command= self.cadastrar)
        submit_button.grid(row=5, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def cadastrar(self):
        assistente_social = self.assistente_social.get()
        instituicoes = self.instituicoes.get()
        aluno_matricula = self.aluno_matricula.get()
        data_encaminhamento = self.data_encaminhamento.get()
        motivo = self.motivo.get()

        self.controller.cadastrar_encaminhamento(assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo)

    def limpar_campos(self):
        self.assistente_social.set("")
        self.instituicoes.set("")
        self.aluno_matricula.set("")
        self.data_encaminhamento.set("")
        self.motivo.set("")
