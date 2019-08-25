from tkinter import *
def play():
    import Play_song
def search():
    import Song_Finder
def support():
    import SupportUs
root5=Tk()
ws=root5.winfo_screenwidth()
hs=root5.winfo_screenheight()
h=550
w=700
x=(ws/2)-(w/2)
y=(hs/2)-(h/2)
root5.geometry('%dx%d+%d+%d'%(w,h,x,y))
root5.title("Beat Finder")
root5.configure(background="silver")
label1=Label(root5,text="BEAT-FINDER",font="algerian 15 bold italic",bg="silver")
label1.place(x=10,y=10)
label2=Label(root5,text="Let's find your beat!",font=("times 10 bold"),bg="silver")
label2.place(x=10,y=50)
label3=Label(root5,text="Play Your Favourite Music",font="times 15 bold",bg="silver")
label3.pack(pady=(100,10))
button1=Button(root5,text="Play",fg="blue",bg="white",font=("times 12 bold"),command=play)
button1.pack()
label4=Label(root5,text="Source For The Songs You Have\nNEVER HEARD Before",font="times 15 bold",bg="silver")
label4.pack(pady=(40,10))
button2=Button(root5,text="Search",fg="blue",bg="white",font=("times 12 bold"),command=search)
button2.pack()
label5=Label(root5,text="Help Other Music Lovers\nFind Their Music",font="times 15 bold",bg="silver")
label5.pack(pady=(40,10))
button3=Button(root5,text="Support Us",fg="blue",bg="white",font=("times 12 bold"),command=support)
button3.pack()
photo1=PhotoImage(file="symbol1.png")
label6=Label(root5,image=photo1)
label6.place(x=0,y=200)
photo=PhotoImage(file="symbol2.png")
label7=Label(root5,image=photo)
label7.place(x=500,y=300)
label8=Label(root5, text="One good thing about music,\nwhen it hits you, you feel no pain\n                  -Bob Marley",font="arial 10 italic",bg="silver")
label8.pack(side=BOTTOM, anchor=E)

root5.mainloop()
