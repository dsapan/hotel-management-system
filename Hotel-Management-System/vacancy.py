from tkinter import *
import mysql.connector

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1400x600+30+30')

# heading
heading_label = Label(root, text="---------  ALL VACANCIES  ---------", bg="deep sky blue", fg="white", font=('Times New Roman', 15,'bold'))
heading_label.pack(fill=X)
title_label = Label(root, text="", height=1,fg='white',font=('Times New Roman', 15,'bold'), bg="medium blue")
title_label.pack(fill=X)
root.configure(background='alice blue')

top_frame = Frame(root)
top_frame.pack()
top_frame.configure(background='alice blue')

# label
o_label = Label(top_frame, text='OCCUPIED', fg='red', font=('Orbitron', 25))
u_label = Label(top_frame, text='UN-OCCUPIED', fg='green', font=('Orbitron', 25))
o_label.grid(row=0, column=0)
u_label.grid(row=0, column=1)

# text bar
text_o = Text(top_frame, bd=5, fg="red", width=48, bg='#b3ffe6', font=('Teko SemiBold', 20),background='lavender')
text_o.grid(row=1, column=0)

text_u = Text(top_frame, bd=5, fg="green", width=67, bg='#b3ffe6', font=('Teko SemiBold', 20),background='lavender')
text_u.grid(row=1, column=1)

# data Show
#

mydb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
alldb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
cur = mydb.cursor()
allcur = alldb.cursor()
cur.execute('SELECT Room_No from hotel_management')
allcur.execute('SELECT Room_No from room')
result = cur.fetchall()
res= allcur.fetchall()
rooms=[]
for i in res:
    b = list(i)
    rooms.append(b[0])
    rooms=list(map(int,rooms))
print(result)
occupied_rooms = []
for i in result:
    a = list(i)
    occupied_rooms.append(a[0])
    occupied_rooms=list(map(int,occupied_rooms))
c1 = 0
c2 = 0
print(occupied_rooms)
for j in rooms:
    if j in occupied_rooms:
        print("yes")
        text_o.insert(INSERT, str(j))
        text_o.insert(INSERT, "\t")
        c1 = c1 + 1
        if c1 == 6:
            text_o.insert(INSERT, "\n")
            c1 = 0
    else:
        text_u.insert(INSERT, str(j))
        text_u.insert(INSERT, "\t")
        c2 = c2 + 1
        if c2 == 6:
            text_u.insert(INSERT, "\n")
            c2 = 0

root.mainloop()
