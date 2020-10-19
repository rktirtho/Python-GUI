from tkinter import *

root = Tk()
def myClick():
    myLabel = Label(root, text="Clicked")
    myLabel.pack()


root.title("Hawk Eye")


myButton = Button(root, text="Login", padx=30, command=myClick, fg='blue')
myButton.pack()
root.mainloop()



