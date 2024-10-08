import tkinter as tk
from tkinter import messagebox

class AtualizarEscolaView:
    def __init__(self, root, controller, valores):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.valores = valores
        self.master.title("Atualizar Escola")

        self.id_escola = tk.StringVar()
        self.nome_escola = tk.StringVar()
        self.diretor = tk.StringVar() 
        self.endereco = tk.StringVar()
        self.celular = tk.StringVar()

        self.carregar_dados()

        tk.Label(self.master, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        self.id_label = tk.Label(self.master, textvariable=self.id_escola)
        self.id_label.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Escola:").grid(row=1, column=0, padx=10, pady=10)
        self.escola_entry = tk.Entry(self.master, textvariable=self.nome_escola)
        self.escola_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Diretor:").grid(row=2, column=0, padx=10, pady=10)
        self.diretor_entry = tk.Entry(self.master, textvariable=self.diretor) 
        self.diretor_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Endereço:").grid(row=3, column=0, padx=10, pady=10)
        self.endereco_entry = tk.Entry(self.master, textvariable=self.endereco)
        self.endereco_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Celular:").grid(row=4, column=0, padx=10, pady=10)
        self.celular_entry = tk.Entry(self.master, textvariable=self.celular)
        self.celular_entry.grid(row=4, column=1, padx=10, pady=10)
        
        submit_button = tk.Button(self.master, text="Atualizar", command=self.atualizar)
        submit_button.grid(row=5, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def atualizar(self):
        id_escola = self.id_escola.get()
        nome_escola = self.nome_escola.get()
        diretor = self.diretor.get()
        endereco = self.endereco.get()
        celular = self.celular.get()

        self.controller.atualizar_escola(id_escola, nome_escola, diretor, endereco, celular)

    def carregar_dados(self):
        self.id_escola.set(self.valores[0])
        self.nome_escola.set(self.valores[1])
        self.diretor.set(self.valores[2])
        self.endereco.set(self.valores[3])
        self.celular.set(self.valores[4])
