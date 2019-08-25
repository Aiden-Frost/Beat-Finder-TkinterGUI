from tkinter import *
def back():
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()
    b = Button(root,text='ok',command=clear)
    b.pack()

    

def all_children (root) :
    _list = root.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

def clear():
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()
    b1 = Button(root,text='back',command=back)
    b1.pack()
    label = Label(text = "success")
    label.pack()


    
root = Tk()
root.geometry("400x400")
b = Button(root,text='ok',command=clear)
b.pack()
root.mainloop()
