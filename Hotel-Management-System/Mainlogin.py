from subprocess import call
from tkinter import *
import tkinter as tk 
import mysql.connector 
import PIL 
from tkinter import messagebox
from functools import partial
import socket

# calling functions
def click_manager():
    root.withdraw()
    vist.withdraw()
    adst.deiconify()


def clickk_staff():
    root.withdraw()
    vist.withdraw()
    sdst.deiconify()
    


def back():
    adst.withdraw()
    root.deiconify()

def click_checkin():
    call(["python", "cin.py"])


def click_checkout():
    call(["python", "check_out.py"])


def click_roomdetail():
    call(["python", "room_detail.py"])


def click_custdetail():
    call(["python", "customer_detail.py"])


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


def click_connect():
    call(['python', 'offer.py'])


def click_addproperty():
    call(['python','add_property.py'])

def click_modifyproperty():
    call(['python','modify_property.py'])

def click_developers():
    call(['python','developers.py'])

def click_searchcustomer():
     call(['python','searchcustomers.py'])

def click_custdetailid():
    call(['python','customerdetailid.py'])

def click_roomhistory():
    call(['python','roomhistory.py'])



def click_loginpage():
    vist.withdraw()
    adst.withdraw()
    musername_entry.delete(0,END)
    mpassword_entry.delete(0,END)
    musername_entry.focus()
    root.deiconify()






def managerlogin():
    use=musername_entry.get()
    passw=mpassword_entry.get()
    if use == "root" and passw == "abc456":
        adst.withdraw()
        root.withdraw()
        vist.deiconify()
    else:
        messagebox.showerror("Wrong","Invalid Username or Password")
        musername_entry.delete(0,END)
        mpassword_entry.delete(0,END)
        musername_entry.focus()


  
  

def stafflogin():
    suse=susername_entry.get()
    spassw=spassword_entry.get()
    if suse == "admin" and spassw == "abc456":
        sdst.withdraw()
        root.withdraw()
        gist.deiconify()
    else:
        messagebox.showerror("Wrong","Invalid Username or Password")
        susername_enrty.delete(0,END)
        spassword_entry.delete(0,END)
        spassword_entry.focus()


    



"""   Start Window  """
root = Tk(className=" GOLD-FINGER HOTELS ")
root.geometry('1860x1080+0+0')


"""    Start  Window Image  """
C = Canvas(root, bg="blue", height=250, width=300)
image2 = PhotoImage(file="himage.png")
label_for_image = Label(root, image=image2)
label_for_image.place(x=0,y=0,relwidth=1,relheight=1)
C.pack()

""" Start Window Buttons """
manager_login_button = Button(root, text="MANAGER", bg='blue2', fg='white', font=('Times New Roman', 12, 'bold'), width=12,
                    command=click_manager)
manager_login_button.place(x=900,y=70)
staff_login_button = Button(root, text="STAFF", bg='blue2', fg='white', font=('Times New Roman', 12, 'bold'), width=12,
                    height=1,command=clickk_staff)
staff_login_button.place(x=1250,y=70)
 
"""   Manager Login Page   """
adst=Toplevel(root)
adst.title("MANAGER LOGIN  ")
adst.geometry("1860x1080")
adst.withdraw()

lblheading = Label(adst, text ="MANAGER LOGIN", bg='blue2', fg='white', font=('Times New Roman', 15, 'bold'), width=20) 

lblfrstrow = Label(adst, text ="USERNAME -", ) 
lblfrstrow.place(x = 650, y = 200) 
musername_entry = Entry(adst,bd=3, font=('arial', 13, 'bold'), width = 45) 
musername_entry.place(x = 750, y = 200, width = 180) 
lblsecrow = Label(adst, text ="PASSWORD-") 
lblsecrow.place(x = 650, y = 250) 
mpassword_entry = Entry(adst,bd=3, show='*', font=('arial', 13, 'bold'),width = 45) 
mpassword_entry.place(x = 750, y = 250, width=180)
submitbtn = Button(adst, text ="LOGIN", 
                    bg ='blue', fg='white',font=('Times New Roman', 10, 'bold'),command =managerlogin) 
submitbtn.place(x = 670, y = 300, width = 70) 
Cancelbtn = Button(adst, text ="BACK", 
                    bg ='blue', fg='white',font=('Times New Roman', 10, 'bold'), command = back) 
Cancelbtn.place(x = 870, y = 300, width = 70) 

lblheading .place(x=670,y=100)

"""   Staff Login Page    """
sdst=Toplevel(root)
sdst.title("STAFF LOGIN  ")
sdst.geometry("1860x1080")
sdst.withdraw()

lblheading = Label(sdst, text ="STAFF LOGIN", bg='blue2', fg='white', font=('Times New Roman', 15, 'bold'), width=20) 

lblfrstrow = Label(sdst, text ="USERNAME -", ) 
lblfrstrow.place(x = 650, y = 200)
susername_entry = Entry(sdst,bd=5,font=('arial', 13, 'bold'),width = 45) 
susername_entry.place(x = 750, y = 200, width = 180) 
lblsecrow = Label(sdst, text ="PASSWORD-") 
lblsecrow.place(x = 650, y = 250) 
spassword_entry = Entry(sdst,bd=5,show='*', font=('arial', 13, 'bold'),width = 45) 
spassword_entry.place(x = 750, y = 250, width = 180) 
submitbtn = Button(sdst, text ="LOGIN", 
                    bg ='blue', fg='white',font=('Times New Roman', 10, 'bold'), command = stafflogin) 
submitbtn.place(x = 670, y = 300, width = 70) 
Cancelbtn = Button(sdst, text ="BACK", 
                    bg ='blue',fg='white',font=('Times New Roman', 10, 'bold'), command = back) 
Cancelbtn.place(x = 870, y = 300, width = 70) 
lblheading .place(x=670,y=100)

"""     Staff Management Page     """
gist=Toplevel(sdst)
gist.title("---------- STAFF PAGE ----------")
gist.geometry('1920x1080')
gist.withdraw()
#Staff Header
menu_bar = Menu(gist)
gist.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="All Customers", command=click_allcust)
home_menu.add_separator()
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Developers")
help_menu.add_separator()
help_menu.add_command(label="Contact Us", command=click_contact_us)

title_label = Label(gist, text="  GOLD  FINGER  HOTELS", height=2,fg='white',font=('Times New Roman', 18,'bold'), bg="medium blue")
title_label.pack(fill=X)

# Welcome label
welcome_label = Label(gist, text="  WELCOME  ",height=2 ,bg="deep sky blue", fg="white", font=('Times New Roman', 18,'bold'))
welcome_label.pack(fill=X)

gist.configure(background='alice blue')

# image
image3 = PhotoImage(file="top.png")
label_for_imagee = Label(gist, image=image3)
label_for_imagee.pack()

blankspace = Label(gist, text="\n")
blankspace.pack()
# image
# Buttons
cin_button = Button(gist, text="Check In", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                  command=click_checkin  )
cin_button.place(x=700,y=340)
cot_button = Button(gist, text="Check Out", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_checkout )
cot_button.place(x=700,y=390)
rd_button = Button(gist, text="Room Details", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_roomdetail)
rd_button.place(x=700,y=440)
# cd_button = Button(gist, text="Customer Details", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
#                    command=click_custdetail)
# cd_button.place(x=700,y=490)

searchcustomer_button = Button(gist, text="Search Customer via City ", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_searchcustomer)
searchcustomer_button.place(x=700,y=490)

cd_button = Button(gist, text="Customer Details via Id", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_custdetailid)
cd_button.place(x=700,y=540)



"""" Manager Management Page """
vist=Toplevel(adst)
vist.title("------- Manager Page ------")
vist.geometry('1920x1080')
vist.withdraw()


menu_bar = Menu(vist)
vist.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="All Customers", command=click_allcust)
home_menu.add_separator()
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)
home_menu.add_separator()
home_menu.add_command(label="Login Page", command=click_loginpage)

about_menu = Menu(menu_bar)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Developers", command=click_developers)


help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Connect", command=click_connect)
about_menu.add_separator()
help_menu.add_command(label="Contact Us", command=click_contact_us)



# Title label
title_label = Label(vist, text="  GOLD  FINGER  HOTELS", height=2,fg='white',font=('Times New Roman', 18,'bold'), bg="medium blue")
title_label.pack(fill=X)

# Welcome label
welcome_label = Label(vist, text="  WELCOME  ",height=2 ,bg="deep sky blue", fg="white", font=('Times New Roman', 18,'bold'))
welcome_label.pack(fill=X)

vist.configure(background='alice blue')

# image
image1 = PhotoImage(file="top.png")
label_for_image = Label(vist, image=image1)
label_for_image.pack()
blankspace = Label(vist, text="\n")
blankspace.pack()
# Buttons
cin_button = Button(vist, text="Check In", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                    command=click_checkin)
cin_button.place(x=700,y=340)
cot_button = Button(vist, text="Check Out", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                    command=click_checkout)
cot_button.place(x=700,y=390)
rd_button = Button(vist, text="Room Details", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_roomdetail)
rd_button.place(x=700,y=440)
# cd_button = Button(vist, text="Customer Details", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
#                    command=click_custdetail)
# cd_button.place(x=700,y=490)
# exit_button = Button(vist, text="Exit", bg="#ff0000", fg="white", width=20, command=root.quit,
#                      font=('Orbitron', 20, 'bold'))
# exit_button.place(x=700,y=560)
pa_button = Button(vist, text="Add Property", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_addproperty)
pa_button.place(x=700,y=490)
pmodify_button = Button(vist, text="Modify Property", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_modifyproperty)
pmodify_button.place(x=700,y=540)
searchcustomer_button = Button(vist, text="Search Customer via City ", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_searchcustomer)
searchcustomer_button.place(x=700,y=590)

cd_button = Button(vist, text="Customer Details via Id", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_custdetailid)
cd_button.place(x=700,y=640)
rd_button = Button(vist, text="Room History", bg='#000000', fg='white', font=('Times New Roman', 12, 'bold'), width=18,
                   command=click_roomhistory)
rd_button.place(x=700,y=690)






root.mainloop()
