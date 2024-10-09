import tkinter as tk
from controllers import aluno_controller, escola_controller, familia_controller, encaminhamento_controller, assistente_social_controller

class CadastroFamiliaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Tabelas")
        self.root.geometry("300x230")
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)

        alunos_button = tk.Button(self.root, text="Alunos", command= self.executar_controller_aluno)
        alunos_button.grid(row=0, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        escolas_button = tk.Button(self.root, text="Escolas", command= self.executar_controller_escola)
        escolas_button.grid(row=1, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        familias_button = tk.Button(self.root, text="Familias", command= self.executar_controller_familia)
        familias_button.grid(row=2, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        encaminhamentos_button = tk.Button(self.root, text="Encaminhamentos", command= self.executar_controller_encaminhamento)
        encaminhamentos_button.grid(row=3, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

        assistentes_sociais_button = tk.Button(self.root, text="Assistentes Sociais", command= self.executar_controller_assistente_social)
        assistentes_sociais_button.grid(row=4, column=0, pady=10, columnspan=2, padx=10, sticky="nsew")

    def executar_controller_aluno(self):
        aluno_controller.AlunoController(self.root)
    
    def executar_controller_escola(self):
        escola_controller.EscolaController(self.root)

    def executar_controller_familia(self):
        familia_controller.FamiliaController(self.root)

    def executar_controller_encaminhamento(self):
        encaminhamento_controller.EncaminhamentoController(self.root)

    def executar_controller_assistente_social(self):
        assistente_social_controller.AssistenteSocialController(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    menu = CadastroFamiliaView(root)
    root.mainloop()