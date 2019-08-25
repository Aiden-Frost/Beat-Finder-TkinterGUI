from tkinter import *
import tkinter.messagebox
def email_id():
    fr = open(text1.get('1.0',END)[:len(text1.get('1.0',END))-1]+'.txt')
    email = fr.read.split('\n')[0]
    return email
    
def sign():
    root3.destroy()
    import SignUp
def login():
    try:
        fr = open(text1.get('1.0',END)[:len(text1.get('1.0',END))-1]+'.txt')
    except Exception as FileNotFoundError:
        tkinter.messagebox .showinfo(" Error" , "Please check your credentials")
    else:
        password = fr.read().split('\n')[1]
        if entry1.get() == password:
            tkinter.messagebox .showinfo(" Confirmed"," Let's get started.")
            root3.destroy()
            import Main
        else:
            tkinter.messagebox .showinfo(" Error" , "Please check your credentials")
        
root3=Tk()
ws=root3.winfo_screenwidth()
hs=root3.winfo_screenheight()
h=550
w=700
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root3.geometry('%dx%d+%d+%d'%(w,h,x,y))
root3.title("Beat Finder")
root3.configure(background="silver")
label1=Label(root3,text="BEAT-FINDER",font="algerian 15 bold italic",bg="silver")
label1.place(x=10,y=10)
label2=Label(root3,text="Lets find your beat!",font=("times 10 bold"),bg="silver")
label2.place(x=10,y=50)
label3=Label(root3,text="Username:",font="times 10 bold",bg="silver")
text1=Text(root3,height=1,width=20)
label3.place(x=10,y=100)
text1.place(x=100,y=100)
label4=Label(root3,text="Password:",font="times 10 bold",bg="silver")
entry1=Entry(root3,width=26,show="*")
label4.place(x=10,y=160)
entry1.place(x=100,y=160)
label8=Label(root3,text="Dont have an account?",font="times 10",bg="silver")
label8.place(x=10,y=230)
button2=Button(root3,text="sign up",font="times 10",fg="blue",command=sign)
button2.place(x=150,y=230)
photo=PhotoImage(file="Image2.png")
label5=Label(root3,image=photo)
label5.place(x=400,y=10)
label6=Label(root3,text="\"Without music,life would be a mistake\"",font="arial 10 italic",bg="silver")
label7=Label(root3,text="-Friedrich Nietzshe",bg="silver")
label7.place(x=400,y=270)
label6.place(x=400,y=250)
button1=Button(text="Let's go",height=2,width=10,bg="blue",fg="white",command=login)
button1.place(x=300,y=400)
root3.mainloop()
