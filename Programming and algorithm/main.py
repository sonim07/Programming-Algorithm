from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")
root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#2E8B57")


name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
email = StringVar()
contact = StringVar()

# Entries Frame
entries_frame = Frame(root, bg="#E0FFFF")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Impact", 25, "underline"), bg="#E0FFFF", fg="#000000")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

#varibles for labels
labelName = Label(entries_frame, text="Employee Name", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labelName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
labelAge = Label(entries_frame, text="Age", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labelAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
labeldoj = Label(entries_frame, text="Date Of Birth", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labeldoj.grid(row=2, column=0, padx=10, pady=10, sticky="w")
labelEmail = Label(entries_frame, text="Employee Email", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labelEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
labelGender = Label(entries_frame, text="Gender", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labelGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
labelContact = Label(entries_frame, text="Employee Contact No", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labelContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
labelAddress = Label(entries_frame, text="Employee Address", font=("Arial", 14), bg="#E0FFFF", fg="#000000")
labelAddress.grid(row=4, column=0, padx=10, pady=10, sticky="w")

#varibles for text field
txtName = Entry(entries_frame, textvariable=name, font=("Arial", 14), width=30)
txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Arial", 14), width=30)
txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("Arial", 14), width=30)
txtDoj.grid(row=2, column=1, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Arial", 14), width=30)
txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Arial", 14), width=30)
txtContact.grid(row=3, column=3, padx=10, sticky="w")
txtAddress = Text(entries_frame, width=83, height=1, font=("Arial", 14))
txtAddress.grid(row=4, column=1, columnspan=4, padx=10, sticky="w")



#varibles for combo box
comboGender = ttk.Combobox(entries_frame, font=("Arial", 14), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=3, column=1, padx=10, sticky="w")



def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr!!", "Please, Fill all the Text Field..")
        return
    db.insert(txtName.get(),txtAge.get(), txtDoj.get() , txtEmail.get() ,comboGender.get(), txtContact.get(), txtAddress.get(
            1.0, END))
    messagebox.showinfo("Success!!", "Record was saved successfuly")
    clearAll()
    dispalyAll()



def update_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtAddress.get(
            1.0, END) == "":
        messagebox.showerror("Erorr!!", "Please, Fill all the Text Field..")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(
                  1.0, END))
    messagebox.showinfo("Success!!", "Record was updated successfuly")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0, END)


BTN_frame = Frame(entries_frame, bg="#E0FFFF")
BTN_frame.grid(row=6, column=0, columnspan=4, padx=60, pady=20, sticky="w")
BTNAdd = Button(BTN_frame, command=add_employee, text="ADD", width=15, font=("Calibri", 16, "bold"), fg="#000000",
                bg="#708090", bd=0).grid(row=0, column=0)
BTNEdit = Button(BTN_frame, command=update_employee, text="UPDATE", width=15, font=("Calibri", 16, "bold"),
                 fg="#000000", bg="#708090",
                 bd=0).grid(row=0, column=1, padx=10)
BTNDelete = Button(BTN_frame, command=delete_employee, text="REMOVE", width=15, font=("Calibri", 16, "bold"),
                   fg="#000000", bg="#708090",
                   bd=0).grid(row=0, column=2, padx=10)
BTNClear = Button(BTN_frame, command=clearAll, text="CLEAR", width=15, font=("Calibri", 16, "bold"), fg="#000000",
                  bg="#708090",
                  bd=0).grid(row=0, column=3, padx=10)

# Table Frame
tree_frame = Frame(root, bg="#ecf0f1")
tree_frame.place(x=0, y=350, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=10)
tv.heading("5", text="Email")
tv.heading("6", text="Gender")
tv.column("6", width=10)
tv.heading("7", text="Contact")
tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
