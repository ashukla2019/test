from tkinter import *
from functools import partial
import os
import sys
from tkinter import messagebox

class login:

    def __init__(self):
        self.username = ""
        self.password = ""
        #window
        global tkWindow
        tkWindow = Tk()  
        tkWindow.geometry('400x150')  
        tkWindow.title('User Login')

        #username label and text entry box
        usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
        self.username = StringVar()
        usernameEntry = Entry(tkWindow, textvariable=self.username).grid(row=0, column=1)  

        #password label and password entry box
        passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
        self.password = StringVar()
        passwordEntry = Entry(tkWindow, textvariable=self.password, show='*').grid(row=1, column=1)  

        #validateLogin = partial(validateLogin, username, password)

        #login button
        loginButton = Button(tkWindow, text="Login", command=self.validateLogin).grid(row=4, column=0)  

        tkWindow.mainloop()
    
    
    def validateLogin(self):
        print (self.username)
        print (self.password)
        if self.username.get() == "akomal" and self.password.get() == "pattu":
            tkWindow.destroy()
        else:
            messagebox.showinfo("Error", "Invalid Username or password")
        

if __name__ == "__main__":
    login()
