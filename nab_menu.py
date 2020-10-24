from tkinter import Tk, Frame, Menu

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Simple menu")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar)
        file_menu.add_command(label="Open File", command=self.onExit)
        file_menu.add_command(label="Recent Open", command=self.onExit)

        edit_menu = Menu(menubar)
        edit_menu.add_command(label="Undo", command=self.onExit)
        edit_menu.add_command(label="Redu", command=self.onExit)

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Edit", menu=edit_menu)


    def onExit(self):

        self.quit()


def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()