from tkinter import *

# Currency Converter

root = Tk()


def rs_convert():
    # convert rs to dollar
    dollar = float(e1_value.get())*82
    t1.delete("1.0", END)
    t1.insert(END, dollar)

    # convert rs to dirham
    dirham = float(e1_value.get())*23
    t2.delete("1.0", END)
    t2.insert(END, dirham)

    # convert rs to Yuan
    yuan = float(e1_value.get())*12
    t3.delete("1.0", END)
    t3.insert(END, yuan)
    
    Label(root,text="USA Currency").grid(row=3,column=0)
    Label(root,text="Dubai Currency").grid(row=3,column=1)
    Label(root,text="China Currency").grid(row=3,column=2)


root.minsize(200, 200)
root.maxsize(900, 900)

e1_value = StringVar()
e1 = Entry(root, textvariable=e1_value, width=20)

t1 = Text(root, width=20, height=1, border=2)
t2 = Text(root, width=20, height=1, border=2)
t3 = Text(root, width=20, height=1, border=2)

l1 = Label(root, text=" Enter Rupees ")
l2 = Label(root, text=" Dollar ")
l3 = Label(root, text=" Dirham ")
l4 = Label(root, text=" Yuan ")
btn = Button(root, text=" Convert ", command=rs_convert)

l1.grid(row=0, column=0)
e1.grid(row=0, column=1)
btn.grid(row=0, column=2)
l2.grid(row=1, column=0)
l3.grid(row=1, column=1)
l4.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)


root.mainloop()
