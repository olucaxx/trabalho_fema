import tkinter as tk
from tkinter import messagebox

class AtualizarEncaminhamentoView:
    def __init__(self, root, controller, valores):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.valores = valores
        self.master.title("Atualizar Encaminhamento")

        self.id = tk.StringVar() 
        self.assistente_social = tk.StringVar()
        self.instituicoes = tk.StringVar() 
        self.aluno_matricula = tk.StringVar()
        self.data_encaminhamento = tk.StringVar()
        self.motivo = tk.StringVar()

        self.carregar_dados()

        tk.Label(self.master, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.id_label = tk.Label(self.master, textvariable=self.id)
        self.id_label.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Assistente Social:").grid(row=1, column=0, padx=10, pady=10)
        self.assistente_social = tk.Entry(self.master, textvariable=self.assistente_social)
        self.assistente_social.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Instituições:").grid(row=2, column=0, padx=10, pady=10)
        self.instituicoes = tk.Entry(self.master, textvariable=self.instituicoes) 
        self.instituicoes.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Matricula:").grid(row=3, column=0, padx=10, pady=10)
        self.aluno_matricula = tk.Entry(self.master, textvariable=self.aluno_matricula)
        self.aluno_matricula.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Data Encaminhamento:").grid(row=4, column=0, padx=10, pady=10)
        self.data_encaminhamento = tk.Entry(self.master, textvariable=self.data_encaminhamento)
        self.data_encaminhamento.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Motivo:").grid(row=5, column=0, padx=10, pady=10)
        self.motivo = tk.Entry(self.master, textvariable=self.motivo)
        self.motivo.grid(row=5, column=1, padx=10, pady=10)


        submit_button = tk.Button(self.master, text="Atualizar", command=self.atualizar)
        submit_button.grid(row=6, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def atualizar(self):
        id = self.id.get()
        assistente_social = self.assistente_social.get()
        instituicoes = self.instituicoes.get()
        aluno_matricula = self.aluno_matricula.get()
        data_encaminhamento = self.data_encaminhamento.get()
        motivo = self.motivo.get()

        self.controller.atualizar_encaminhamento(id, assistente_social, instituicoes, aluno_matricula, data_encaminhamento, motivo)

    def carregar_dados(self):
        self.id.set(self.valores[0])
        self.assistente_social.set(self.valores[1])
        self.instituicoes.set(self.valores[2])
        self.aluno_matricula.set(self.valores[3])
        self.data_encaminhamento.set(self.valores[4])
        self.motivo.set(self.valores[5])
