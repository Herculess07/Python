from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Marksheets")
root.minsize(500, 300)
root.maxsize(600, 300)


def calculate():
	Label(root, text="Congratulations!!!").grid(row=0, column=3)

	e1_get = float(e1_value.get())
	e2_get = float(e2_value.get())
	e3_get = float(e3_value.get())
	e4_get = float(e4_value.get())
	e5_get = float(e5_value.get())
	e6_get = float(e6_value.get())
	e7_get = float(e7_value.get())
	e8_get = float(e8_value.get())

	tot_int = e1_get + e2_get + e3_get + e4_get
	tot_ext = e5_get + e6_get + e7_get + e8_get
	total = tot_int + tot_ext
	percent = 100 * total / 400

	nosql = e1_get + e5_get
	# android = e2_get + e6_get
	# python = e3_get + e7_get
	# cdp2 = e4_get + e8_get

	t4.delete("1.0", END)
	t4.insert(END, total)

	t5.delete("1.0", END)
	t5.insert(END, percent)

	if (nosql >= 90):
		t3_gr_nos.delete("1.0", END)
		t3_gr_nos.insert(END, "A")
	elif (80 <= nosql >= 70):
		t3_gr_nos.delete("1.0", END)
		t3_gr_nos.insert(END, "B")
	else:
		t3_gr_nos.delete("1.0", END)
		t3_gr_nos.insert(END, "Try")



# Labels
l1 = Label(root, text=" Marksheet ", font=25).grid(row=0, column=3)
l2 = Label(root, text=" Student Name  ").grid(row=1, column=2)
l3 = Label(root, text=" Enrollnment No  ").grid(row=2, column=2)
l_no = Label(root, text="No.").grid(row=3, column=0)
l4 = Label(root, text="Sub. Code").grid(row=3, column=1)
l5 = Label(root, text="Subjects").grid(row=3, column=2)


l5_scode4 = Label(root, text=" P22A1ND ").grid(row=4, column=1)
l5_scode5 = Label(root, text=" P22A3AAD ").grid(row=5, column=1)
l5_scode6 = Label(root, text=" P22A2PYT ").grid(row=6, column=1)
l5_scode7 = Label(root, text=" P22B4CDP2 ").grid(row=7, column=1)

l5_s1 = Label(root, text=" NO SQL ").grid(row=4, column=2)
l5_s2 = Label(root, text=" Android ").grid(row=5, column=2)
l5_s3 = Label(root, text=" Python ").grid(row=6, column=2)
l5_s4 = Label(root, text=" CDP2 ").grid(row=7, column=2)

l6 = Label(root, text=" Internal Marks(40) ").grid(row=3, column=3)
l7 = Label(root, text=" External Marks(60) ").grid(row=3, column=4)

l8 = Label(root, text=" Grade ").grid(row=3, column=5)

l9 = Label(root, text=" Total Marks ").grid(row=8, column=2)
l10 = Label(root, text=" Percentage ").grid(row=9, column=2)

# Entries (User Inputs)
e1_name = Entry(root, width=20).grid(row=1, column=3)
e1_enroll = Entry(root, width=20).grid(row=2, column=3)

e1_value = StringVar()
e2_value = StringVar()
e3_value = StringVar()
e4_value = StringVar()
e5_value = StringVar()
e6_value = StringVar()
e7_value = StringVar()
e8_value = StringVar()

e1_in_nos = Entry(root, textvariable=e1_value, width=10).grid(row=4, column=3)
e1_in_and = Entry(root, textvariable=e2_value, width=10).grid(row=5, column=3)
e1_in_pyt = Entry(root, textvariable=e3_value, width=10).grid(row=6, column=3)
e1_in_cdp = Entry(root, textvariable=e4_value, width=10).grid(row=7, column=3)

e2_ex_nos = Entry(root, textvariable=e5_value, width=10).grid(row=4, column=4)
e2_ex_and = Entry(root, textvariable=e6_value, width=10).grid(row=5, column=4)
e2_ex_pyt = Entry(root, textvariable=e7_value, width=10).grid(row=6, column=4)
e2_ex_cdp = Entry(root, textvariable=e8_value, width=10).grid(row=7, column=4)

t3_gr_nos = Text(root, width=4, height=1)
t3_gr_nos.grid(row=4, column=5)
t3_gr_and = Text(root, width=4, height=1)
t3_gr_and.grid(row=5, column=5)
t3_gr_pyt = Text(root, width=4, height=1)
t3_gr_pyt.grid(row=6, column=5)
t3_gr_cdp = Text(root, width=4, height=1)
t3_gr_cdp.grid(row=7, column=5)

# progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate').grid(row=9, column=4)
# btn2 = Button(root, text="progress", command=progress).grid(row=8, column=4)
# Texts (displays for show data)

t4 = Text(root, width=10, height=1)  # Total
t5 = Text(root, width=10, height=1)  # Percentage
t4.grid(row=8, column=3)
t5.grid(row=9, column=3)
btn = Button(root, text="Calculate", command=calculate).grid(row=8, column=5)

for i in range(1, 5):
	Label(root, text=i).grid(row=3 + i, column=0)

root.mainloop()
