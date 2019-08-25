from tkinter import *
import re
import tkinter.messagebox
import smtplib
import random
def email_id():
    fr = open(text1.get('1.0',END)[:len(text1.get('1.0',END))-1]+'.txt')
    email = fr.read.split('\n')[0]
    return email
def confirm():
    if int(check.entry1.get()) == check.otp:
        check.root1.destroy()
        tkinter.messagebox .showinfo(" Confirmed" , "Successfully created your account\n Let's get started.")
        root.destroy()
        import Main
    else:
        tkinter.messagebox .showinfo(" Error" , "Please check the One time Password")
        
def check():
    if text3.get('1.0',END)==text4.get('1.0',END):
        if len(text3.get('1.0',END)) >=8 and re.search(r"\d", text3.get('1.0',END))!=None and re.search(r"[A-Z]", text3.get('1.0',END))!=None and re.search(r"[a-z]", text3.get('1.0',END))!=None and re.search(r"[ !#@$%&'()*+,-./[\\\]^_`{|}~"+r'"]', text3.get('1.0',END))!=None:
            fw = open(text1.get('1.0',END)[:len(text1.get('1.0',END))-1]+".txt",'w')
            fw.write(text2.get('1.0',END)+text3.get('1.0',END))
            fw.close()
            check.otp = random.randint(1000,9999)
            message = "Welcome to the communtiy of Music lovers.\nYou are just one step away.\nYour One Time Password is"+' '+':'+' '+str(check.otp)
            email_user = 'beat.finder.music@gmail.com'
            email_send = text2.get('1.0',END)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,'beat@123')
            server.sendmail(email_user,email_send,message)
            server.quit()
            check.root1 = Tk()
            check.root1.title("Verification")
            ws = check.root1.winfo_screenwidth() 
            hs = check.root1.winfo_screenheight() 
            h = 100
            w=300
            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            check.root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
            label9= Label(check.root1,text="Please check you email for One Time Password")
            label9.place(x=10,y=10)
            check.entry1 = Entry(check.root1)
            check.entry1.place(x=90,y=40)
            button1 = Button(check.root1,text="Verify",command=confirm)
            button1.place(x=130,y=70)
            check.root1.mainloop()
                
        else:
            tkinter.messagebox .showinfo(' Error' , 'Please check the Password you have entered.')
root = Tk()
root.title("Beat Finder")
ws = root.winfo_screenwidth() 
hs = root.winfo_screenheight() 
h =550
w=700
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
label1 = Label(root,text="Beat-Finder",font=("algerian",15,"bold"))
label1.place(x=10,y=10)
label2 = Label(root,text="Create Your Account",font=("times",15,"bold"))
label2.place(x=10,y=50)
label3 = Label(root,text="Username",font=("times",12,"bold"))
label3.place(x=10,y=100)
text1 = Text(root,height=1,width=20)
text1.place(x=100,y=100)
label4 = Label(root,text="Email-ID",font=("times",12,"bold"))
label4.place(x=10,y=140)
text2 = Text(root,height=1,width=30)
text2.place(x=100,y=140)
label4 = Label(root,text="Password",font=("times",12,"bold"))
label4.place(x=10,y=180)
text3 = Text(root,height=1,width=20)
text3.place(x=100,y=180)
label5 = Label(root,text="Confirm",font=("times",12,"bold"))
label5.place(x=300,y=180)
text4 = Text(root,height=1,width=20)
text4.place(x=390,y=180)
label6 = Label(root,text="Use 8 or more characters with a mix of letters , numbers and symbols.",font=("times",12,"bold"),fg="grey")
label6.place(x=10,y=220)
photo = PhotoImage(file='Image.png')
label7 = Label(root,image=photo)
label7.place(x=250,y=250)
label8 = Label(root,text="You are just one step away from finding the music of your heart",font=("times",12,"bold"))
label8.place(x=180,y=440)
button1 = Button(text="Sign Up",height=2,width=10,command=check)
button1.place(x=300,y=480)
root.mainloop()
