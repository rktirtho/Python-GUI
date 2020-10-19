from tkinter import *

root = Tk()
userName = Entry(root, width=50)
# give value in box
userName.insert(1, "User Name")
userName.pack()


def login_click():
    euser = userName.get()
    if euser == "234":
        status = Label(root, text="userName exist").pack()
    else:
        status = Label(root, text="userName Does not exist").pack()


btnLogin = Button(root,text="Login", command=login_click)
btnLogin.pack()
root.mainloop()
