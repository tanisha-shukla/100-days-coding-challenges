print("    DESIGNING GUI LOGIN  FORM  \n")

from tkinter  import *
def check():
    username = nametxt.get()
    password = pwdtxt.get()
    print("username entered : ", username)
    print("password  entered : ", password)

# window
win = Tk ()
win.geometry("400x150")
win.title("Login  Form ")

#username
name = Label(win, text ="User Name ")
name.grid(row=0 , column=0)
nametxt = Entry(win)
nametxt.grid(row=0 , column=1)

#password
pwd = Label(win , text= "Password")
pwd.grid(row=1 , column=0)
pwdtxt = Entry(win , show = "*")
pwdtxt.grid(row=1 , column=1)


#login button
btnlogin = Button(win , text = "Login" , command=check)
btnlogin.grid(row=3 , column=0)

win.mainloop()



