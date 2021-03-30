from tkinter import *
import tkinter as tk 
root=Tk()
root.title("DEVELOPERS")
root.geometry("1860x1080+0+0")
root.configure(background='alice blue')

lblTemp=Label(root,text="NAME - SAPAN .DAS",font=("Times New Roman",18,'bold italic'))
lblTemPp=Label(root,text="NAME - DHRUVI.JAIN ",font=("Times New Roman",18,'bold italic'))

lblTemp.place(x=100,y=100)
lblTemPp.place(x=100,y=150)

root.mainloop()