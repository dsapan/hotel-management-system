from tkinter import *
import mysql.connector
from tkinter import scrolledtext

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1080x900')

# heading
heading_label = Label(root, text="---------  ALL CUSTOMERS  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

top_frame = Frame(root)
top_frame.pack()

# customer text view
text = scrolledtext.ScrolledText(root, bd=5, bg="white", fg='blue', width=200,height=300, font=('Arial', 13))
text.place(rely=0.1)

# database
mydb = mysql.connector.connect(host='localhost', user='root', password='abc456', database='hotel')
cur = mydb.cursor()
cur.execute('SELECT * from hotel_management')
result = cur.fetchall()
title = "Cust Id\t\tFirst Name\t\tPhone No\t\tCity Name\t\tRoom No\t\tRoom Type\n"
text.insert(INSERT, title)
formatting = "-------------------------------------------------------------------------------------------" \
             "-------------------------------------------------------------------------------------------" \
             "------------------------------------------------------------------------------------------\n"
text.insert(INSERT, formatting)
text.insert(INSERT, formatting)
for i in result:
    d = list(i)

    s = str(d[0])+"\t\t"+ d[1]+"\t\t" +d[3]+ "\t\t"+d[5]+ "\t\t"+str(d[6])+"\t\t"+d[7]+"\t\t"+"\n\n\n"
    text.insert(INSERT, s)
    text.insert(INSERT, formatting)

root.mainloop()
