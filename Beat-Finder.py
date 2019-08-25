from tkinter import *
def login():
    root.destroy()
    import Login
def signup():
    root.destroy()
    import SignUp

root = Tk()
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen
h = 550
w=700
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.configure(bg="silver")
label1 = Label(root, text="Beat-Finder", font=("algerian", 50, "bold"),bg="silver")
label1.pack(side=TOP, fill=X, pady=25)
label2 = Label(root, text="Finding the right music for you",bg="silver",font="times 20 bold")
label2.pack()
button1 = Button(root, text="Login", font="times 10 bold",width=20, height=3, relief=RAISED,bg="blue",fg="white",command=login)
button1.pack(pady=25)
button2 = Button(root, text="Sign Up",font="times 10 bold" ,width=20, height=3,bg="blue",fg="white",command=signup)
button2.pack()

root.mainloop()
