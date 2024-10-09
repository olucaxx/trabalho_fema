import tkinter as tk
from tkinter import messagebox

class AtualizarAssistenteView:
    def __init__(self, root, controller, valores):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.valores = valores
        self.master.title("Atualizar Assistente Social")
        self.master.resizable(False, False)

        self.id_assistente_social = tk.StringVar()
        self.nome = tk.StringVar()
        self.celular = tk.StringVar()

        self.carregar_dados()

        tk.Label(self.master, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.id_label = tk.Label(self.master, textvariable=self.id_assistente_social)
        self.id_label.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Nome:").grid(row=1, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.master, textvariable=self.nome)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Celular:").grid(row=2, column=0, padx=10, pady=10)
        self.celular_entry = tk.Entry(self.master, textvariable=self.celular)
        self.celular_entry.grid(row=2, column=1, padx=10, pady=10)
        
        submit_button = tk.Button(self.master, text="Atualizar", command=self.atualizar)
        submit_button.grid(row=3, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def atualizar(self):
        id_assistente_social = self.id_assistente_social.get()
        nome = self.nome.get()
        celular = self.celular.get()

        self.controller.atualizar_assistente_social(id_assistente_social, nome, celular)

    def carregar_dados(self):
        self.id_assistente_social.set(self.valores[0])
        self.nome.set(self.valores[1])
        self.celular.set(self.valores[2])
