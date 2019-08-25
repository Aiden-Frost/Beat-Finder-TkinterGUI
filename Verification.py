from tkinter import *
def confirm():
    verification_code = entry1.get()
root1 = Tk()
root1.title("Verification")
ws = root1.winfo_screenwidth() 
hs = root1.winfo_screenheight() 
h = 100
w=300
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
label9= Label(root1,text="Please check you email for One Time Password")
label9.place(x=10,y=10)
entry1 = Entry(root1)
entry1.place(x=90,y=40)
button1 = Button(root1,text="Verify",command=confirm)
button1.place(x=130,y=70)
root1.mainloop()


