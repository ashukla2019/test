import sqlite3
from datetime import date
import Tkinter as tk
from Tkinter import *
import ttk
import tkMessageBox

def printData():
	conn = sqlite3.connect('mydb.db')
	print "Opened database successfully";
	cursor = conn.execute("SELECT id, name, Date from Emp")
	#Create a vertical scrollbar
	win = Tk()

	#Set the geometry of Tkinter Frame
	win.geometry("700x350")
	scrollbar= ttk.Scrollbar(win, orient= 'vertical')
	scrollbar.pack(side= RIGHT, fill= BOTH)

	#Add a Listbox Widget
	listbox = Listbox(win, width= 350, bg= 'bisque')
	listbox.pack(side= LEFT, fill= BOTH)

	for row in cursor:  
		test_string = "Product NAME-> " + row[1] + "Expiry Date " + row[2]
		listbox.insert(END, test_string)  
		
	listbox.config(yscrollcommand= scrollbar.set)
	#Configure the scrollbar
	scrollbar.config(command= listbox.yview)

  
	today = date.today()
	print("Today's date:", today)
		
	# show date in different format
	today = today.strftime("%d/%m/%Y")
	print("Today's date:", today)

	if(row[2] == today):
		print "product is expiring"
		tkMessageBox.showerror("Title", "Message")

	print row[2]
	print today
	conn.close()
	
def insertData(name, expiry_date):
	
	conn = sqlite3.connect('mydb.db')
	sqlite_insert_with_param = """INSERT INTO Emp
                          (NAME, Date) 
                          VALUES (?, ?);"""
	data_tuple = (name, expiry_date)
	conn.execute(sqlite_insert_with_param, data_tuple)
	conn.commit()


#	conn.execute("DELETE from Emp where ID = 3;")
#	conn.commit()