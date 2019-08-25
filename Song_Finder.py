from tkinter import *
import Songs
import smtplib
import tkinter.messagebox
def home():
    root7.destroy()
def email():
    message = "Here are the few songs we suggest \n"
    for i in range(len(Songs.artists)):
        if Songs.artists[i]==str(var.get()) and str(var1.get())==Songs.genre[i]:
            message+="Artist : "+Songs.artists[i]+"    "+"Song : "+Songs.song[i]+"    "+"Genre :"+Songs.genre[i]+"\n"
    email_user = 'beat.finder.music@gmail.com'
    email_send = genre.entry1.get()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,'beat@123')
    server.sendmail(email_user,email_send,message)
    server.quit()
    tkinter.messagebox .showinfo(" Success" , "Please check your email for our suggestion :)")

    
def genre():
    global var1
    label4 = Label(root7,text="Your preferred Genre",font=("times 12 bold"))
    label4.place(x=300,y=240)
    var1 = StringVar(root7)
    var1.set('select')
    genres = Songs.genre
    genre_choices=[]
    for i in range(len(Songs.artists)):
        if Songs.artists[i]==str(var.get()):
            genre_choices.append(genres[i])
    genre_choices=list(set(genre_choices))
    option1 = OptionMenu(root7, var1, *genre_choices)
    option1.place(x=320,y=270)
    label5 = Label(root7,text="E-mail_ID",font=("times 12 bold"))
    label5.place(x=260,y=310)
    genre.entry1 = Entry(root7,width=40)
    genre.entry1.place(x=370,y=310)
    button2 = Button(root7,text="Suggest me",command=email)
    button2.place(x=340,y=340)
root7=Tk()
ws=root7.winfo_screenwidth()
hs=root7.winfo_screenheight()
h=550
w=700
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root7.geometry('%dx%d+%d+%d'%(w,h,x,y))
root7.title("Beat Finder")
label1=Label(root7,text="BEAT-FINDER",font="algerian 15 bold italic")
label1.place(x=10,y=10)
label2=Label(root7,text="Lets find your beat!",font=("times 10 bold"))
label2.place(x=10,y=50)
label3 = Label(root7,text="Your Preferred Artisit",font=("times 12 bold"))
label3.place(x=300,y=100)
button = Button(root7,text="Home",height=1,width=10,font=("times 12 bold"),command=home)
button.place(x=300,y=50)
var = StringVar(root7)
var.set('select')
artist_choices = (list(set(Songs.artists)))
option = OptionMenu(root7, var, *artist_choices)
option.place(x=320,y=130)
button1 = Button(root7,text="Confirm",command=genre)
button1.place(x=340,y=170)
