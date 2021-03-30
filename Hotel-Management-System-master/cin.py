
from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox
from tkinter import scrolledtext

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1500x800')


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
F_name = StringVar()
L_name = StringVar()
Phone = StringVar()
C_name = StringVar()
Address = StringVar()
Room_no = IntVar()
room_info = StringVar()
room_ratentry=StringVar()
room_descentry=StringVar()
No_people = StringVar()
No_days = StringVar()
Checked_out=StringVar()



# Database Submitted
def click_submit():
    f_name = F_name.get()
    l_name = L_name.get()
    phone = Phone.get()
    c_name = C_name.get()
    address = Address.get()
    room_no = Room_no.get()
    no_people = No_people.get()
    room_type=room_info.get(1.0,END)
    room_rate=room_ratentry.get(1.0,END)
    no_days = No_days.get()
    room_desc=room_descentry.get(1.0,END)
    checked_out=Checked_out.get()
    if f_name == '' or l_name == '' or phone == 0  or address == '' or c_name== '' or room_no == 0 \
            or no_people == 0 or room_type == '' or no_days == 0:
        messagebox.showwarning("Warning", "Incomplete Data Entry")
    else:
        mydb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
        alldb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
        allcur = alldb.cursor()
        cur = mydb.cursor()
        cur.execute('Select Exists(select * from hotel_management where Room_No=%s)', (room_no,))
        res = cur.fetchall()
        avail = 0
        for i in res:
            a = list(i)
            avail = a[0]
        if avail == 0:
            cur.execute('INSERT INTO hotel_management'
                        '(First_Name, Last_Name, Phone_No, Address_No,City_Name ,Room_No, Room_Type, No_People, '
                        'No_Days,checked_out,Room_Rate,Room_Desc) '
                        ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (f_name, l_name, phone, address,c_name, room_no, room_type, no_people, no_days,checked_out,room_rate,room_desc))
            allcur.execute('INSERT INTO all_data'
                           '(First_Name, Last_name, Phone_No, Address_No,City_Name, Room_No, Room_Type, No_People, '
                           'No_Days,checked_out,Room_Rate,Room_Desc) '
                           ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           (f_name, l_name, phone, address,c_name, room_no, room_type, no_people, no_days,checked_out,room_rate,room_desc))
            mydb.commit()
            alldb.commit()
            # if no_people == 2:
            #     call(['python', 'second_person.py'])

            fname_entry.delete(0, 'end')
            lname_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            city_entry.delete(0,'end')
            ad_entry.delete(0, 'end')
            rn_entry.delete(0, 'end')

            messagebox.showinfo("Check in", "Room Allotment Successful")
            root.destroy()
        else:
            messagebox.showinfo("Room", "Room Already Occupied")
            rn_entry.delete(0, 'end')

def click_roomcheck():
    room_info.delete(1.0,"end")
    room_ratentry.delete(1.0,"end")
    room_descentry.delete(1.0,"end")
    room_no = Room_no.get()
    roomdb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
    alldet = roomdb.cursor()
   
    alldet.execute('select Room_Type,Room_Rate,Room_Desc from room where Room_No=%s', (room_no,))
    rez = alldet.fetchall()
    for i in rez:
        tup = list(i)
    info=tup[0];
    zinfo=tup[1]
    xinfo=tup[2]
    print(zinfo)
    room_info.insert(INSERT,info)
    room_ratentry.insert(INSERT,zinfo)
    room_descentry.insert(INSERT,xinfo)
     
               
  



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
heading_label = Label(root, text="---------  CUSTOMER CHECK IN FORM  ---------",bg="deep sky blue", fg="white", font=('Times New Roman', 15,'bold'))
heading_label.pack(fill=X)
title_label = Label(root, text="", height=1,fg='white',font=('Times New Roman', 15,'bold'), bg="medium blue")
title_label.pack(fill=X)

black_space = Label(root, text="\n\n")
black_space.pack()

# form Design
root.configure(background='alice blue')


top_frame = Frame(root)
top_frame.pack()
top_frame.configure(background='alice blue')

# Name Label
fname_label = Label(top_frame, text="First Name : ", font=('Times New Roman', 20,"bold"))
lname_label = Label(top_frame, text="Last Name : ", font=('Times New Roman', 20,"bold"))
fname_entry = Entry(top_frame, textvar=F_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
lname_entry = Entry(top_frame, bd=5, textvar=L_name, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

fname_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)
lname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
fname_entry.grid(row=0, column=1, pady=10, ipady=5, ipadx=60)
lname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)

# phone number
phone_label = Label(top_frame, text="Mobile Number : ", font=('Times New Roman', 20,"bold"))
phone_entry = Entry(top_frame, textvar=Phone, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

phone_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
phone_entry.grid(row=2, column=1, ipady=5, ipadx=60)

# Email Address
# email_label = Label(top_frame, text="Email Address : ", font=('Orbitron', 20))
# email_entry = Entry(top_frame, textvar=Email, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

# email_label.grid(row=3, column=0, padx=15, pady=10, sticky=E)
# email_entry.grid(row=3, column=1, ipady=5, ipadx=60)

# Address
ad_label = Label(top_frame, text=" Address : ", font=('Times New Roman', 20,"bold"))
ad_entry = Entry(top_frame, bd=5, textvar=Address, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

ad_label.grid(row=3, column=0, padx=15, pady=10, sticky=E)
ad_entry.grid(row=3, column=1, ipady=5, ipadx=60)

#City Name
city_label = Label(top_frame, text="City Name : ", font=('Times New Roman', 20,"bold"))
city_entry = Entry(top_frame, bd=5, textvar=C_name,bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

city_label.grid(row=4, column=0, padx=15, pady=10, sticky=E)
city_entry.grid(row=4, column=1, ipady=5, ipadx=60)

# Room Number

rn_label = Label(top_frame, text="Room Number : ", font=('Times New Roman', 20,"bold"))
rn_entry = Entry(top_frame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=5, font=('Arial', 15))

rn_label.grid(row=5, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=5, column=1, ipady=5, ipadx=60, sticky=W)

# Number of Days
day_label = Label(top_frame, text="Number of Days : ",font=('Times New Roman', 20,"bold"))
day_box = Spinbox(top_frame, textvar=No_days, bg="#ccefff", fg='blue', from_=1, to=30, width=5, bd=5,
                  font=('Orbitron', 15))



day_label.grid(row=6, column=0, padx=15, pady=10, sticky=E)
day_box.grid(row=6, column=1, ipady=5, sticky=W)



# room Type
room_label =room_label = Label(top_frame, text="Room Type : ", font=('Times New Roman', 20,"bold"))
room_info = Text(top_frame,width=5,height=2,   fg='blue', font=('Arial', 13, 'bold'))

room_ratelabel=Label(top_frame, text="Room Rate : ", font=('Times New Roman', 20,"bold"))
room_ratentry = Text(top_frame,width=5,height=2,   fg='blue', font=('Arial', 13, 'bold'))

room_desclabel=Label(top_frame, text="Room Desc : ", font=('Times New Roman', 20,"bold"))
room_descentry = Text(top_frame,width=13,height=2,   fg='blue', font=('Arial', 13, 'bold'))

# ac_rb = Radiobutton(top_frame, variable=Room_type, text="AC Room", fg='blue', font=('Arial', 12, 'bold'), value=1)
# nac_rb = Radiobutton(top_frame, variable=Room_type, text="Non-AC Room", fg='blue', font=('Arial', 12, 'bold'), value=2)

room_label.grid(row=7, column=0, padx=12, pady=10, sticky=E)
room_info.grid(row=7, column=1, sticky=W)
room_ratelabel.grid(row=7, column=1, padx=12, pady=10, sticky=E)
room_ratentry.grid(row=7, column=2,  sticky=W)
room_desclabel.grid(row=7, column=4, padx=12, pady=10, sticky=E)
room_descentry.grid(row=7, column=5,  sticky=W)
# nac_rb.grid(row=7, column=1, sticky=E)

# Number of Person
per_label = Label(top_frame, text="Number of People : ", font=('Times New Roman', 20,"bold"))
per_box = Spinbox(top_frame, textvar=No_people, bg="#ccefff", fg='blue', from_=1, to=2, width=5, bd=5,
                  font=('Orbitron', 15))

checkout_label = Label(top_frame, text="Checkout Date: ", font=('Times New Roman', 20,"bold"))
checkout_entry = Entry(top_frame, textvar=Checked_out, bd=5, bg="#ccefff", fg='blue', width=10, font=('Arial', 15))

per_label.grid(row=8, column=0, padx=15, pady=10, sticky=E)
per_box.grid(row=8, column=1, ipady=5, sticky=W)

checkout_label.grid(row=9, column=0, padx=12, pady=10, sticky=E)
checkout_entry.grid(row=9, column=1, ipady=5, sticky=W)

# vacancy Button
v_button = Button(top_frame, text="Vacancy", font=('ARIAL BLACK', 12,"bold"), bg='deep sky blue',
                  fg='black', width=6, command=click_vacancy)
v_button.grid(row=5, column=1, ipadx=7, sticky=E)

c_button = Button(top_frame, text="Fetch", font=('ARIAL BLACK', 12,"bold"), bg='deep sky blue',
                  fg='black', width=6, command=click_roomcheck)
c_button.grid(row=5, column=3, ipadx=8, sticky=W)

# Submit Button
submit_button = Button(root, text="SUBMIT", width=10, bg="medium blue", fg='white', font=('ARIAL BLACK', 20), relief=RAISED,
                       command=click_submit)
submit_button.place(relx=0.5, rely=0.95, anchor=S)



root.mainloop()
