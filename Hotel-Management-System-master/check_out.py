from subprocess import call
from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter import scrolledtext

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1020x700+200+2')


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
# L_name = StringVar()
Room_no = IntVar()


# Database Update
def click_proceed():
    f_name = F_name.get()
    # l_name = L_name.get()
    room_no = Room_no.get()

    if f_name == ''  or room_no == 0:
        messagebox.showwarning("Warning", "Incomplete Data Entry")

    else:
        text.delete('1.0', END)
        mydb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
        cur = mydb.cursor()

        cur.execute('Select Exists(select * from hotel_management where First_Name=%s  and Room_No=%s)',
                    (f_name,  room_no))
        res = cur.fetchall()
        avail = 0
        for i in res:
            a = list(i)
            avail = a[0]
        if avail == 1:
            cur.execute('SELECT * from hotel_management where Room_no=%s',
                        (room_no,))
            bill_detail = cur.fetchall()
            for d in bill_detail:
                price=str(int(d[12])*int(d[9]))
                final_detail = "\nCustomer Id : \t"+ str(d[0])+"\t\tRoom No : \t"+ str(d[6])+"\n\n"+"First Name : \t " + d[1] + "\t\t Last Name  : \t "+d[2]+ "\n\n"+"Room Type : \t"+ d[7] +"\n\n"+"Booked for Days : "+d[9]+"\t\t\tRoom Rate(Rs) : "+d[12]+"\n\n"+"Checked In Date & Time : "+str(d[10])+"\n\n"+"Total Cost(Rs): "+price+"\n\nRoom Desc : "+d[13]+"\n\n"+"Checked Out:\t"+str(d[11])+"\n"
            cur.execute('DELETE from hotel_management where Room_no =%s', (room_no,))
            mydb.commit()

            fname_entry.delete(0, 'end')
            # lname_entry.delete(0, 'end')
            rn_entry.delete(0, 'end')

            # bill detail
            text.insert(INSERT, "\t\tYou Have successfully checked out --- Kindly Make the payment at counter\n\n")
            text.insert(INSERT,final_detail )
            formatting = "---------------------------------------------------------------" \
                         "---------------------------------------------------------------" \
                         "-----------------------------------------------------------------\n"
            text.insert(INSERT, formatting)
            text.insert(INSERT, formatting)
            # bill = []
            # print(bill_detail)
            # for i in bill_detail:
            #     bill = list(i)
            #     string_bill = "First Name :\t " + bill[0] + "\n" + "Last Name :\t " + bill[1] + "\n"
            #     text.insert(INSERT, string_bill)
            # s1 = "Room Number :\t " + str(bill[2]) + "\n"
            # s2 = "Number of Days :\t " + str(bill[3]) + "\n"
            # s3 = "Room Type :\t " + str(bill[4]) + "\n"
            # text.insert(INSERT, s1)
            # text.insert(INSERT, s2)
            # if bill[4] == 1:
            #     amount = bill[3] * 2000
            # else:
            #     amount = bill[3] * 1500
            # s4 = "\nTotal Amount To Be Paid : \t" + str(amount)
            # text.insert(INSERT, s4)

        else:
            fname_entry.delete(0, 'end')
            # lname_entry.delete(0, 'end')
            rn_entry.delete(0, 'end')
            text.insert(INSERT, "INVALID DATA !!!!!!!\t\t Please Enter Correct Details   !!!!!")


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
heading_label = Label(root, text="---------  CUSTOMER CHECK OUT FORM  ---------", bg="deep sky blue", fg="white", font=('Times New Roman', 15,'bold'))
heading_label.pack(fill=X)
title_label = Label(root, text="", height=1,fg='white',font=('Times New Roman', 15,'bold'), bg="medium blue")
title_label.pack(fill=X)

black_space = Label(root, text="\n\n")
black_space.pack()
root.configure(background='alice blue')

# form Design


top_frame = Frame(root)
top_frame.pack()
top_frame.configure(background='alice blue')


# Name Label
fname_label = Label(top_frame, text="First Name : ", font=('Times New Roman', 20,"bold"))
# lname_label = Label(top_frame, text="Last Name : ",  font=('Times New Roman', 20,"bold"))
fname_entry = Entry(top_frame, textvar=F_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
# lname_entry = Entry(top_frame, textvar=L_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

fname_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)
# lname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
fname_entry.grid(row=0, column=1, pady=10, ipady=5, ipadx=60)
# lname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)

# Room Number

rn_label = Label(top_frame, text="Room Number : ",  font=('Times New Roman', 20,"bold"))
rn_entry = Entry(top_frame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=5, font=('Arial', 15))

rn_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=2, column=1, ipady=5, ipadx=60, sticky=W)

# Proceed Button
proceed_button = Button(root, text="PROCEED", width=16, bg="medium blue", fg='White', font=('ARIAL BLACK', 15),
                        relief=RAISED, command=click_proceed)
proceed_button.place(relx=0.5, rely=0.45, anchor=S)

# Billing
text = scrolledtext.ScrolledText(root, bd=3, bg="white", fg='blue', height=16,width=98, font=('Times New Roman', 15,"bold"))
text.place(rely=0.50)

root.mainloop()
