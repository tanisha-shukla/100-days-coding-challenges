# Code to make a login screen using -- tkinter --- 
print("     GUI  INTERFACE  \n " )

from tkinter  import *

def greet1():
	n = nam.get()
	p = pw.get()
	if n == "abc" and  p =="123":
		lres.configure(text="Welcome  " + n )
	else:
		lres.configure(text="Invalid Username or Password ")

def greet2():
	n = nam.get()
	lres.configure(text="Bye " + n)

parent = Tk() # parent is a variable name to create an object  of  a window  
parent.geometry("400x250")
parent.title("Login Form") # this will show the title

l1 = Label(parent , text = "Name : ")
l1.place(x=10 , y=50)
nam = Entry(parent)
nam.place(x=90 , y=50)

l2 = Label(parent , text = "Password : ")
l2.place(x=10 , y=100)
pw = Entry(parent)
pw.place(x=90 , y=100)


lres = Label(parent , text ="MESSAGE ")
lres.place(x = 90 , y = 190 )
tfv = Label(parent , text = "Thanks For Visiting")
tfv.place(x = 150 , y= 230)

b1 = Button(parent,text="Login" , command = greet1)
b1.place(x = 30 , y = 140)
b2 = Button(parent,text="Logout" , command = greet2)
b2.place(x = 100 , y = 140)

parent.mainloop() # line to stop  a code


