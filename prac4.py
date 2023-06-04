from tkinter import *
from tkinter import ttk

root = Tk()

# root.title("This is Title")
# inpBox = Label(root,text="This is Label")
# inpBox.pack()

# text = Text(root,width=10,height=1)
# text.pack()

fName = Entry(root)
lName = Entry(root)

Label(root, text="First Name").pack()
fName.pack()
Label(root, text="Last Name").pack()
lName.pack()

button = Button(root,width=10,height=1,text="Stop",command=root.destroy,activebackground="Yellow",activeforeground="red",bg="red",fg="yellow",border=2,font="verdana")
button.pack()

root.mainloop()