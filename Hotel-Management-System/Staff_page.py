from subprocess import call
from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT ")
root.geometry('1920x1080')

def click_checkin():
    call(["python", "check_in.py"])


def click_checkout():
    call(["python", "check_out.py"])


def click_roomdetail():
    call(["python", "room_detail.py"])


def click_custdetail():
    call(["python", "customer_detail.py"])


# Buttons
cin_button = Button(root, text="Check In", bg='#000000', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                  command=click_checkin   )
cin_button.pack(pady=5)
cot_button = Button(root, text="Check Out", bg='#1a1a1a', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                   command=click_checkout )
cot_button.pack(pady=5)
rd_button = Button(root, text="Room Details", bg='#404040', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                  command=click_roomdetail )
rd_button.pack(pady=5)
cd_button = Button(root, text="Customer Details", bg='#666666', fg='white', font=('Orbitron', 20, 'bold'), width=20,
                  command=click_custdetail )
cd_button.pack(pady=5)
exit_button = Button(root, text="Exit", bg="#ff0000", fg="white", width=20,
                     font=('Orbitron', 20, 'bold'))
exit_button.pack(pady=5)


root.mainloop()
