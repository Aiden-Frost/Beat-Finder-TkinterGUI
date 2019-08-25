from tkinter import *
import tkinter.messagebox
def home():
    root4.destroy()
def submit():
    fa = open("music.txt","a")
    fa.write('\n'+entry1.get()+'\t'+entry2.get()+'\t'+entry3.get())
    fa.close()
    tkinter.messagebox .showinfo(" Success" , "Thank you for the suggestion.")
root4=Tk()
ws=root4.winfo_screenwidth()
hs=root4.winfo_screenheight()
h=550
w=700
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root4.geometry('%dx%d+%d+%d'%(w,h,x,y))
root4.title("Beat Finder")
label1=Label(root4,text="BEAT-FINDER",font="algerian 15 bold italic")
label1.place(x=10,y=10)
label2=Label(root4,text="Lets find your beat!",font=("times 10 bold"))
label2.place(x=10,y=50)
button = Button(root4,text="Home",height=1,width=10,font=("times 12 bold"),command=home)
button.place(x=300,y=50)
label1 = Label(root4,text="Artist :",font=("times 12 bold"))
label1.place(x=150,y=200)
entry1 = Entry(root4,width=40)
entry1.place(x=200,y=200)
label2 = Label(root4,text="Song :",font=("times 12 bold"))
label2.place(x=150,y=240)
entry2 = Entry(root4,width=40)
entry2.place(x=200,y=240)
label3 = Label(root4,text="Genre :",font=("times 12 bold"))
label3.place(x=150,y=280)
entry3 = Entry(root4,width=40)
entry3.place(x=200,y=280)
button1 = Button(root4,text="Submit",font=("times 12 bold"),command=submit)
button1.place(x=300,y=330)


