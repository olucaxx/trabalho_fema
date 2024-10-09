import tkinter as tk
from tkinter import messagebox

class AtualizarAlunoView:
    def __init__(self, root, controller, valores):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.valores = valores
        self.master.title("Atualizar Aluno")
        self.master.resizable(False, False)

        self.matricula = tk.StringVar()
        self.id_escola = tk.StringVar()
        self.id_familia = tk.StringVar() 
        self.nome = tk.StringVar()
        self.data_nasc = tk.StringVar()
        self.endereco = tk.StringVar()
        self.responsavel = tk.StringVar()

        self.carregar_dados() 

        tk.Label(self.master, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.id_label = tk.Label(self.master, textvariable=self.matricula)
        self.id_label.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="ID Escola:").grid(row=1, column=0, padx=10, pady=10)
        self.escola_entry = tk.Entry(self.master, textvariable=self.id_escola)
        self.escola_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="ID Família:").grid(row=2, column=0, padx=10, pady=10)
        self.familia_entry = tk.Entry(self.master, textvariable=self.id_familia) 
        self.familia_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Nome:").grid(row=3, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.master, textvariable=self.nome)
        self.nome_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Data Nasc:").grid(row=4, column=0, padx=10, pady=10)
        self.nascimento_entry = tk.Entry(self.master, textvariable=self.data_nasc)
        self.nascimento_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Endereço:").grid(row=5, column=0, padx=10, pady=10)
        self.endereco_entry = tk.Entry(self.master, textvariable=self.endereco)
        self.endereco_entry.grid(row=5, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Responsável:").grid(row=6, column=0, padx=10, pady=10)
        self.responsavel_entry = tk.Entry(self.master, textvariable=self.responsavel)
        self.responsavel_entry.grid(row=6, column=1, padx=10, pady=10)
        
        submit_button = tk.Button(self.master, text="Atualizar", command=self.atualizar)
        submit_button.grid(row=7, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def atualizar(self):
        matricula = self.matricula.get()
        id_escola = self.id_escola.get()
        id_familia = self.id_familia.get()
        nome = self.nome.get()
        data_nasc = self.data_nasc.get()
        endereco = self.endereco.get()
        responsavel = self.responsavel.get()

        self.controller.atualizar_aluno(matricula, id_escola, id_familia, nome, data_nasc, endereco, responsavel)

    def carregar_dados(self):
        self.matricula.set(self.valores[0])
        self.id_escola.set(self.valores[1])
        self.id_familia.set(self.valores[2])
        self.nome.set(self.valores[3])
        self.data_nasc.set(self.valores[4])
        self.endereco.set(self.valores[5])
        self.responsavel.set(self.valores[6])
