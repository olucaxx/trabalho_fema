import tkinter as tk
from tkinter import messagebox

class CadastroEscolaView:
    def __init__(self, root, controller):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.master.title("Cadastro Escola")
        self.master.resizable(False, False)

        self.nome_escola = tk.StringVar()
        self.diretor = tk.StringVar() 
        self.endereco = tk.StringVar()
        self.celular = tk.StringVar()

        tk.Label(self.master, text="Escola:").grid(row=0, column=0, padx=10, pady=10)
        self.escola_entry = tk.Entry(self.master, textvariable=self.nome_escola)
        self.escola_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Diretor:").grid(row=1, column=0, padx=10, pady=10)
        self.diretor_entry = tk.Entry(self.master, textvariable=self.diretor) 
        self.diretor_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Endereço:").grid(row=2, column=0, padx=10, pady=10)
        self.endereco_entry = tk.Entry(self.master, textvariable=self.endereco)
        self.endereco_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Celular:").grid(row=3, column=0, padx=10, pady=10)
        self.celular_entry = tk.Entry(self.master, textvariable=self.celular)
        self.celular_entry.grid(row=3, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.master, text="Cadastrar", command= self.cadastrar)
        submit_button.grid(row=4, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def cadastrar(self):
        nome_escola = self.nome_escola.get()
        diretor = self.diretor.get()
        endereco = self.endereco.get()
        celular = self.celular.get()

        self.controller.cadastrar_escola(nome_escola, diretor, endereco, celular)

    def limpar_campos(self):
        self.nome_escola.set("")
        self.diretor.set("")
        self.endereco.set("")
        self.celular.set("")
