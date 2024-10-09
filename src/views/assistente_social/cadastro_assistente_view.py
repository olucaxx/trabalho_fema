import tkinter as tk
from tkinter import messagebox

class CadastroAssistenteView:
    def __init__(self, root, controller):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.master.title("Cadastro Assistente Social")
        self.master.resizable(False, False)

        self.nome = tk.StringVar()
        self.celular = tk.StringVar()

        tk.Label(self.master, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.master, textvariable=self.nome)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Celular:").grid(row=1, column=0, padx=10, pady=10)
        self.celular_entry = tk.Entry(self.master, textvariable=self.celular)
        self.celular_entry.grid(row=1, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.master, text="Cadastrar", command= self.cadastrar)
        submit_button.grid(row=2, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def cadastrar(self):
        nome = self.nome.get()
        celular = self.celular.get()

        self.controller.cadastrar_assistente_social(nome, celular)

    def limpar_campos(self):
        self.nome.set("")
        self.celular.set("")
