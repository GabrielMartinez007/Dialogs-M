from tkinter import *
from tkinter.ttk import *
from docx import *



class Control():
    def __init__(self, tk_root):
        tk_root.geometry("600x620")
        tk_root.config(bg="#292929")
        tk_root.title("Dialogs-M")
        self.menuBar(tk_root)

        MainFrame(tk_root,
            self.mainFrameS(),
            self.MLabelFrameS(),
            )

    def mainFrameS(self):
        MFS = Style()
        MFS.configure('MFS.TFrame',
            background="#ffffff"
            )
        return MFS

    def MLabelFrameS(self):
        LFS = Style()
        LFS.configure('lfs.TLabelframe',
        background="#ffffff"
            )

        LFS.configure('lfs.TLabelframe.Label',
            Foreground="#ffffff",
            background="#ffffff",
            font=("cambria", 13)
            )

        return LFS

    def menuBar(self, parent):
        self.menuBar = Menu(parent)
        parent.config(menu=self.menuBar)
        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.archivoMenu.add_command(label="Nuevo", command=lambda:self.Nuevo())
        self.archivoMenu.add_command(label="Guardar", command=lambda:self.Guardar())
        self.archivoMenu.add_command(label="Guardar como", command=lambda:self.SaveAs())
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Salir", command=lambda:self.Salir())
        self.preMenu = Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label= "Preferencias", menu=self.preMenu)
        self.preMenu.add_command(label="Temas", command=lambda:self.temas())
        self.preMenu.add_command(label="Fondos", command=lambda:self.imagen())


class MainFrame():
    def __init__(self, root, Fstyle, Lstyle):
        MFrame = Frame(
            root,
            width=580,
            height=600,
            style="MFS.TFrame"
            )

        MFrame.place(x=10, y=10)

        MLabelFrame = LabelFrame(
            MFrame,
            text="Caracteristicas del documento",
            width=560, heigh=550,
            style="lfs.TLabelframe"
            )

        MLabelFrame.place(y=40, x=10)

        Inside(root,)


class Inside():
    def __init__(self, Mframe, style=()):
        self.mainFrameL(Mframe)

    def mainFrameL(self, parent):
        Label(
            parent,
            text="Rellena los siguientes espacios con la informacion correspondiente.",
            font=("cambria", 14),
            background="#ffffff"
            ).place(x=20, y=10)



if __name__ == '__main__':
    tk = Tk()
    Control(tk)
    tk.mainloop()
