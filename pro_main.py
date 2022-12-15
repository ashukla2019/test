import datetime
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry  # pip install tkcalendar
import sqlite3
from datetime import datetime
from datetime import date

# Creating the universal font variables
headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

# Connecting to the Database where all information will be stored
connector = sqlite3.connect('Product.db')
cursor = connector.cursor()
connector.execute(
"CREATE TABLE IF NOT EXISTS Product (Product_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, PRODUCTTYPE TEXT, DOP TEXT, DOE TEXT)"
)

# Creating the functions
def reset_fields():
   global name_strvar, ptype_strvar, dop, doe
   for i in ['name_strvar', 'ptype_strvar']:
       exec(f"{i}.set('')")
   #dop.set_date(datetime.datetime.now().date())
   #doe.set_date(datetime.datetime.now().date())
   
def check_expiry():
	today = str(date.today())
	print("Today's date:", today)
	tree.delete(*tree.get_children())
	curr = connector.execute('SELECT * FROM Product')
	data = curr.fetchall()
	
	for row in data:
		print(row[1])  
		if(row[4] < today):
			mb.showerror('Error!', row[1]+"is expired")
		
def reset_form():
   global tree
   tree.delete(*tree.get_children())
   reset_fields()
   
def display_records():
   tree.delete(*tree.get_children())
   curr = connector.execute('SELECT * FROM Product')
   data = curr.fetchall()
   for records in data:
       tree.insert('', END, values=records)
       
 
def add_record():
   global name_strvar, ptype_strvar, dop, doe
   name = name_strvar.get()
   ptype = ptype_strvar.get()
   DOP = dop.get_date()
   DOE = doe.get_date()
   
   if not name or not ptype or not DOP or not DOE:
       mb.showerror('Error!', "Please fill all the missing fields!!")
   else:
       try:
           connector.execute(
           'INSERT INTO Product (NAME, PRODUCTTYPE, DOP, DOE) VALUES (?,?,?,?)', (name, ptype, DOP, DOE)
           )
           connector.commit()
           mb.showinfo('Record added', f"Record of {name} was successfully added")
           print("p1")
           reset_fields()
           print("p2")
           display_records()
           print("p3")
       except:
           mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')

def remove_record():
   if not tree.selection():
       mb.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = tree.focus()
       values = tree.item(current_item)
       selection = values["values"]
       tree.delete(current_item)
       connector.execute('DELETE FROM Product WHERE STUDENT_ID=%d' % selection[0])
       connector.commit()
       mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')
       display_records()

def view_record():
   global name_strvar, ptype_strvar, dop, doe
   if not tree.selection():
       mb.showerror('Error!', 'Please select a record to view')
   else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        name_strvar.set(selection[1]); ptype_strvar.set(selection[2])
        date = datetime.date(int(selection[3][:4]), int(selection[3][3:7]), int(selection[3][8:]))
        dop.set_date(date);doe.set_date(date)


# Initializing the GUI window
main = Tk()
main.title('Product Management System')
main.geometry('1000x800')
main.resizable(0, 0)

# Creating the background and foreground color variables
lf_bg = 'MediumSpringGreen' # bg color for the left_frame
cf_bg = 'PaleGreen' # bg color for the center_frame

# Creating the StringVar or IntVar variables
name_strvar = StringVar()
ptype_strvar = StringVar()

# Placing the components in the main window
Label(main, text="Product Management System", font=headlabelfont, bg='SpringGreen').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.3)

right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.3, y=30, relheight=1, relwidth=0.8)


# Placing components in the left frame
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.075, rely=0.01)
Label(left_frame, text="Type", font=labelfont, bg=lf_bg).place(relx=0.075, rely=0.06)
Label(left_frame, text="Date of Purchase (DOP)", font=labelfont, bg=lf_bg).place(relx=0.075, rely=0.15)
Label(left_frame, text="Date of Expiry (DOE)", font=labelfont, bg=lf_bg).place(relx=0.075, rely=0.23)

#Data Entry 
Entry(left_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.03)
OptionMenu(left_frame, ptype_strvar, 'Food', 'Medicine').place(x=20, rely=0.10, relwidth=0.45)
dop = DateEntry(left_frame, font=("Arial", 12), width=15)
dop.place(x=20, rely=0.19)
doe = DateEntry(left_frame, font=("Arial", 12), width=15)
doe.place(x=20, rely=0.27)

Button(left_frame, text='Delete Record', font=labelfont, command=remove_record, width=15).place(relx=0.025, rely=0.35)
Button(left_frame, text='View Record', font=labelfont, command=view_record, width=15).place(relx=0.025, rely=0.40)
Button(left_frame, text='Reset Fields', font=labelfont, command=reset_fields, width=15).place(relx=0.025, rely=0.45)
Button(left_frame, text='Delete database', font=labelfont, command=reset_form, width=15).place(relx=0.025, rely=0.50)
Button(left_frame, text='Submit and Add Record', font=labelfont, command=add_record, width=18).place(relx=0.025, rely=0.55)
Button(left_frame, text='Check Expiry of product', font=labelfont, command=check_expiry, width=18).place(relx=0.025, rely=0.60)

# Placing components in the center frame


# Placing components in the right frame
Label(right_frame, text='Students Records', font=headlabelfont, bg='DarkGreen', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                   columns=('Student ID', "Name", "Type", "Date of Purchase", "Date of Expiry"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Type', text='Type', anchor=CENTER)
tree.heading('Date of Purchase', text='DOP', anchor=CENTER)
tree.heading('Date of Expiry', text='DOE', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()

# Finalizing the GUI window
main.update()
main.mainloop()
