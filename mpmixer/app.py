import tkinter as tk

from .controllers import MainController


def main():
    root = tk.Tk()
    MainController(root)
    root.mainloop()
