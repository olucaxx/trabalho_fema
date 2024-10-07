import tkinter as tk
from controllers import escola_controller

if __name__ == "__main__":
    root = tk.Tk()
    controller = escola_controller.EscolaController(root)
    root.mainloop()
    