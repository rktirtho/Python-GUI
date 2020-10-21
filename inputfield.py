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

#
# import kinter as tk
#
# root=tk.Tk()
# f1 = tk.Frame(width=200, height=200, background="red")
# f2 = tk.Frame(width=100, height=100, background="blue")
#
# f1.pack(fill="both", expand=True, padx=20, pady=20)
# f2.place(in_=f1, anchor="c", relx=.5, rely=.5)
#
# root.mainloop()
