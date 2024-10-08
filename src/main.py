import tkinter as tk
from controllers import encaminhamento_controller

if __name__ == "__main__":
    root = tk.Tk()
    controller = encaminhamento_controller.EncaminhamentoController(root)
    root.mainloop()
    