from tkinter import *
import subprocess
from subprocess import call
import os
import shutil 
import time
from tkinter import Tk, Label, Button
import sys
from tkcalendar import Calendar

class GUI:
    def __init__(self, master):
        os.system('login.py')
        self.setUI(master)
    
    def setUI(self, master):
        self.frame = Frame (root)
        self.frame.pack()

        self.label = Label(self.frame, text= "Welcome to Project", bg = "green", width= 80, height= 2)
        self.label.pack()

        self.button1 = Button (self.frame, text = "Product Details",command=self.product_details, fg="blue", bg="green", width= 50, height=4)
        self.button1.pack()

        self.button2 = Button (self.frame, text="Setup_Synergy", command=self.close_window, fg="blue", bg="green", width= 50, height=4)
        self.button2.pack()

        self.button3 = Button (self.frame, text="Setup_object_Ada", command=self.close_window, fg="blue", bg="green", width= 50, height=4)
        self.button3.pack()

        self.button4 = Button (self.frame, text="Download BaseLine", command=self.close_window, fg="blue", bg="green", width= 50, height=4)
        self.button4.pack()

        self.button5 = Button (self.frame, text="Build code", command=self.close_window, fg="blue", bg="green", width= 50, height=4)
        self.button5.pack()
        
    def product_details(self):
        os.system('main_db.py')
        
    def close_window(self):
        sys.exit()


    
root = Tk()
root.geometry("1800x800")
app = GUI(root)
root.mainloop()


    


