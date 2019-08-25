import Songs
from tkinter import *
import webbrowser
def home():
    root4.destroy()
def listen():
    pos = Songs.song.index(str(song.var1.get()))
    webbrowser.open(Songs.link[pos])
    
def song():
    label4 = Label(root4,text="Select the song of the artist",font=("times 12 bold"))
    label4.place(x=270,y=240)
    song.var1 = StringVar(root4)
    song.var1.set('select')
    songs = Songs.song
    song_choices=[]
    for i in range(len(Songs.artists)):
        if Songs.artists[i]==str(var.get()):
            song_choices.append(songs[i])
    option1 = OptionMenu(root4, song.var1, *song_choices)
    option1.place(x=320,y=270)
    button2 = Button(root4,text="Listen",command=listen)
    button2.place(x=340,y=310)
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
label3 = Label(root4,text="Select your Artist",font=("times 12 bold"))
label3.place(x=300,y=100)
var = StringVar(root4)
var.set('select')
artist_choices = (list(set(Songs.artists)))
option = OptionMenu(root4, var, *artist_choices)
option.place(x=320,y=130)
button1 = Button(root4,text="Confirm",command=song)
button1.place(x=340,y=170)

