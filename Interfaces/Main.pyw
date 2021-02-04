from tkinter import Tk
from tkinter import ttk
from docx import *



class Root():
    def __init__(self, tk_root, style):
        tk_root.geometry("600x620")
        tk_root.config(bg="#292929")
        tk_root.title("Dialogs-M")
        MainFrame(tk_root,)

class Styles():
    def __init__(self):
        self.MainFrameS()

    def MainFrameS(self):
        MainFrameStyle = ttk.Style()
        MainFrameStyle.configure('MF.TFrame', background="#ffffff")

        return MainFrameStyle



class MainFrame():
    def __init__(self, root):
        MFrame = ttk.Frame(root, width=580, height=600)
        MFrame.place(x=10, y=10)

if __name__ == '__main__':
    tk = Tk()
    estilos = Styles()
    Root(tk, estilos)
    tk.mainloop()
