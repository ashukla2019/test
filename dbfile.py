import sqlite3
from datetime import date
import tkinter as tk
from tkinter import *
from tkinter import ttk
#import tkMessageBox

def printData():
	conn = sqlite3.connect('mydb.db')
	print ("Opened database successfully")
	cursor = conn.execute("SELECT name, ExpiryDate from Products")
	
	for row in cursor:  
		test_string = "Product NAME-> " + row[1] + "Expiry Date " + row[2]
		print (test_string)
  
	conn.close()
	
def insertData(name, expiry_date):
	
	conn = sqlite3.connect('mydb.db')
	sqlite_insert_with_param = """INSERT INTO Products
                          (NAME, ExpiryDate) 
                          VALUES (?, ?);"""
	data_tuple = (name, expiry_date)
	conn.execute(sqlite_insert_with_param, data_tuple)
	conn.commit()
	
def checkProductExpiryValue():
	today = str(date.today())
	print("Today's date:", today)
	conn = sqlite3.connect('mydb.db')
	print ("Opened database successfully")
	cursor = conn.execute("SELECT name, ExpiryDate from Products")
	
	for row in cursor:  
		if(row[1] < today):
			print (row[0] + " is expiried")
		
  
	conn.close()

#	conn.execute("DELETE from Emp where ID = 3;")
#	conn.commit()
