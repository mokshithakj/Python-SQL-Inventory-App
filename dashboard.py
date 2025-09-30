from tkinter import *

root= Tk()
root.title("Python SQL Inventory")
root.geometry("1270x668")
root.config(background = "#f8e9d2")
icon=PhotoImage(file="inventory.png")
titlelabel=Label(root,text="Inventory Management Systems",image=icon,compound=LEFT,font=("Arial",30,"bold"),background="pink",fg="white")
titlelabel.place(x=0,y=0,relwidth=1)


root.mainloop()