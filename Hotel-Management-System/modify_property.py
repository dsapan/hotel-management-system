from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1020x700+200+20')


# calling functions
def click_vacancy():
    call(["python", "vacancy.py"])


def click_developers():
    call(["python", "developers.py"])


def click_branches():
    call(["python", "branches.py"])


def click_contact_us():
    call(["python", "contact_us.py"])


def click_staff():
    call(["python", "staff.py"])


def click_allcust():
    call(['python', 'all_details.py'])


# variables
# F_name = StringVar()
# L_name = StringVar()
# Phone = IntVar()
# Email = StringVar()
# Address = StringVar()
# Room_no = IntVar()
# Room_type = IntVar()
# Room_type.set(1)
# No_people = IntVar()
# No_days = IntVar()
Pid=IntVar()
Property_loc=StringVar()
No_rooms=IntVar()


# Database Submitted
def click_submit():
    # f_name = F_name.get()
    # l_name = L_name.get()
    # phone = Phone.get()
    # email = Email.get()
    # address = Address.get()
    # room_no = Room_no.get()
    # no_people = No_people.get()
    # room_type = Room_type.get()
    # no_days = No_days.get()
    ploc=Property_loc.get()
    prooms=No_rooms.get()
    pid=Pid.get()

    if ploc == '' or prooms== 0 or pid=='' or pid==0 :
        messagebox.showwarning("Warning", "Incomplete or Wrong Data Entry")

    else:
        mydb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
        cur = mydb.cursor()
        cur.execute('Select Exists(select * from property where pid=%s)', (pid,))
        res = cur.fetchall()
        avail = 0
        for i in res:
            a = list(i)
            avail = a[0]
        if avail == 0:
            cur.execute('UPDATE property SET prooms = %s,ploc=%s WHERE pid = %s',(prooms,ploc,pid) )
            mydb.commit()
            mydb.close()
            cur.close()
            propertyname_entry.delete(0, 'end')
            noofrooms_entry.delete(0, 'end')
            pid_entry.delete(0,'end')
            messagebox.showinfo("Successfull", "Property Details Modified!!")
            root.destroy()
        else:

            messagebox.showinfo("Check Your Details !")
            propertyname_entry.delete(0, 'end')
            noofrooms_entry.delete(0, 'end')
            pid_entry.delete(0,'end')
        


# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="All Customers", command=click_allcust)
home_menu.add_separator()
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

about_menu = Menu(menu_bar)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Branches", command=click_branches)
about_menu.add_separator()
about_menu.add_command(label="Staff", command=click_staff)
about_menu.add_separator()
about_menu.add_command(label="Developers", command=click_developers)

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Contact Us", command=click_contact_us)

# heading
heading_label = Label(root, text="---------  MODIFY PROPERTY  ---------", bg="deep sky blue", fg="white", font=('Times New Roman', 15,'bold'))
heading_label.pack(fill=X)
title_label = Label(root, text="", height=1,fg='white',font=('Times New Roman', 15,'bold'), bg="medium blue")
title_label.pack(fill=X)
root.configure(background='alice blue')

black_space = Label(root, text="\n\n")
black_space.pack()

# form Design

top_frame = Frame(root)
top_frame.pack()
top_frame.configure(background='alice blue')

# Name Label
propertyid_label = Label(top_frame, text="Property Id: ", font=('Times New Roman', 20,"bold"))
propertyname_label = Label(top_frame, text="Property Location: ", font=('Times New Roman', 20,"bold"))
noofrooms_label = Label(top_frame, text="No Of Rooms : ",font=('Times New Roman', 20,"bold"))

pid_entry = Entry(top_frame, bd=5, textvar=Pid, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
propertyname_entry = Entry(top_frame, textvar=Property_loc, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
noofrooms_entry = Entry(top_frame, bd=5, textvar=No_rooms, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

propertyid_label.grid(row=0, column=0, padx=13, pady=10, sticky=E)
propertyname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
noofrooms_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)

pid_entry.grid(row=0, column=1, padx=0, pady=10,ipady=5, ipadx=60 )
propertyname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)
noofrooms_entry.grid(row=2, column=1, pady=10, ipady=5, ipadx=60)




# Submit Button
submit_button = Button(root, text="SUBMIT", width=15, bg="medium blue", fg='White', font=('ARIAL BLACK', 16), relief=RAISED,
                       command=click_submit)
submit_button.place(relx=0.5, rely=0.75, anchor=S)

root.mainloop()
