import Tkinter as tk
from Tkinter import *
import ttk
from dbfile import printData,insertData

class guiWindow:
			
	def __init__(self, master):
		self.master = master
 
		self.pawin = PanedWindow(orient ='horizontal')
		
		btn1 = Button(self.pawin, text="Exit_hello", fg="blue", command=quit)
		btn1.pack(side=LEFT)
				
		btn2 = Button(self.pawin,text="Product_details",fg="red",command=self.product_info)
		btn2.pack(side=LEFT)
		
		self.pawin.add(btn1)
		self.pawin.add(btn2)
		
		self.pawin.pack()
		
		self.frame = Frame(master, width=600, height=400)
		self.frame.pack()
		self.frame.place(anchor='n', relx=0.5, rely=0.2)

		self.label = Label(self.frame, text='Welcome', width=500)
		self.label.config(font=('Helvetica bold', 40))
		self.label.pack()
		
		
	def clear_frame(self):
		for widget in self.frame.winfo_children(): #clearing the frame widget
			widget.destroy()
		
	def product_info(self):
		self.clear_frame()
		
		bt1 = Button(self.frame,text="All Products",fg="red", height=5, width=30, command=self.getProductDetails)
		bt1.place(x=10, y=20)
		bt1.pack(side=TOP)
		
		bt2 = Button(self.frame,text="Add Product",fg="green", height=5, width=30,command=self.addProduct)
		bt2.place(x=20, y=20)
		bt2.pack(side=TOP)
		
	def getProductDetails(self):
		printData()
		
	def addProduct(self):
		root= tk.Tk()
		canvas1 = tk.Canvas(root, width = 400, height = 400,  relief = 'raised')
		canvas1.pack()

		label1 = tk.Label(root, text='Add Product Datails')
		label1.config(font=('helvetica', 14))
		canvas1.create_window(200, 25, window=label1)

		label2 = tk.Label(root, text='Enter product name')
		label2.config(font=('helvetica', 10))
		canvas1.create_window(200, 100, window=label2)

		self.entry1 = tk.Entry (root) 
		canvas1.create_window(200, 140, window=self.entry1)
		
		label3 = tk.Label(root, text='Product Expiry date')
		label3.config(font=('helvetica', 10))
		canvas1.create_window(200, 180, window=label3)

		self.entry2 = tk.Entry (root) 
		canvas1.create_window(200, 220, window=self.entry2)
		
		button1 = tk.Button(root, text='Add details', command=self.add_details, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
		canvas1.create_window(200, 260, window=button1)

	def add_details(self):
		name = self.entry1.get()
		date = self.entry2.get()
		insertData(name, date)
	
         
app = tk.Tk()
#getting screen width and height of display
width= app.winfo_screenwidth()
height= app.winfo_screenheight()

#setting tkinter window size
app.geometry("%dx%d" % (width, height))

window = guiWindow(app)
app.mainloop()