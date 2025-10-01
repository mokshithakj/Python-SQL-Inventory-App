from tkinter import *
from tkinter import PhotoImage

from sqlalchemy import column

root= Tk()

root.title("Python SQL Inventory System")
root.geometry("1270x668")
root.config(background = "#f8e9d2")

icon=PhotoImage(file="inventory.png")
titlelabel=Label(root,text="Inventory Management Systems",image=icon,compound=LEFT,font=("times new roman",25),background="pink",fg="black")
titlelabel.place(x=0,y=0,relwidth=1)

logoutbutton=Button(root,text="LOG OUT",font=("times new roman",12,"bold"),compound="right",background="#c43d5b",fg="white")
logoutbutton.place(x=1150,y=20,)

sublabel=Label(root,text="Welcome User ",font=("times new roman",15),background="#88b89b",fg="white")
sublabel.place(x=0,y=70,relwidth=1)




sidelabel=Label(root,background="#f4a873")
sidelabel.place(x=0,y=100,width=250,height=600)

menulabel=Label(sidelabel,text="MENU",font=("times new roman",15),background="#f4a873")
menulabel.pack(fill=X)

emp_button=Button(menulabel,text="EMPLOYEE",font="times new roman",background="pink")
root.mainloop()




