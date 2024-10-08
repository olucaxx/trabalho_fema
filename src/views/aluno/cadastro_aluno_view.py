import tkinter as tk
from tkinter import messagebox

#        self.tabela.heading('matricula', text='Matricula', anchor='w')
 #       self.tabela.heading('id_escola', text='ID Escola', anchor='w')
  #      self.tabela.heading('id_familia', text='ID Família', anchor='w')
   #     self.tabela.heading('nome', text='Nome', anchor='w')
    #    self.tabela.heading('data_nasc', text='Data Nasc', anchor='w')
     #   self.tabela.heading('endereco', text='Endereço', anchor='w')
      #  self.tabela.heading('responsavel', text='Responsável', anchor='w')

class CadastroAlunoView:
    def __init__(self, root, controller):
        self.master = tk.Toplevel(root)
        self.controller = controller
        self.master.title("Cadastro Aluno")

        self.id_escola = tk.StringVar()
        self.id_familia = tk.StringVar() 
        self.nome = tk.StringVar()
        self.data_nasc = tk.StringVar()
        self.endereco = tk.StringVar()
        self.responsavel = tk.StringVar()

        tk.Label(self.master, text="ID Escola:").grid(row=0, column=0, padx=10, pady=10)
        self.escola_entry = tk.Entry(self.master, textvariable=self.id_escola)
        self.escola_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.master, text="ID Família:").grid(row=1, column=0, padx=10, pady=10)
        self.familia_entry = tk.Entry(self.master, textvariable=self.id_familia) 
        self.familia_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Nome:").grid(row=2, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.master, textvariable=self.nome)
        self.nome_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Data Nasc:").grid(row=3, column=0, padx=10, pady=10)
        self.nascimento_entry = tk.Entry(self.master, textvariable=self.data_nasc)
        self.nascimento_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Endereço:").grid(row=4, column=0, padx=10, pady=10)
        self.endereco_entry = tk.Entry(self.master, textvariable=self.endereco)
        self.endereco_entry.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(self.master, text="Responsável:").grid(row=5, column=0, padx=10, pady=10)
        self.responsavel_entry = tk.Entry(self.master, textvariable=self.responsavel)
        self.responsavel_entry.grid(row=5, column=1, padx=10, pady=10)

        submit_button = tk.Button(self.master, text="Cadastrar", command= self.cadastrar)
        submit_button.grid(row=6, column=0, pady=20, columnspan=2, padx=10, sticky="nsew")

    def mostrar_alerta(self, mensagem):
        messagebox.showwarning("ALERTA", mensagem)

    def cadastrar(self):
        id_escola = self.id_escola.get()
        id_familia = self.id_familia.get()
        nome = self.nome.get()
        data_nasc = self.data_nasc.get()
        endereco = self.endereco.get()
        responsavel = self.responsavel.get()

        self.controller.cadastrar_aluno(id_escola, id_familia, nome, data_nasc, endereco, responsavel)

    def limpar_campos(self):
        self.id_escola.set("")
        self.id_familia.set("")
        self.nome.set("")
        self.data_nasc.set("")
        self.endereco.set("")
        self.responsavel.set("")
