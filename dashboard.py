from tkinter import *
from tkinter import PhotoImage

def employeeform():
    emp_frame=Frame(root,width=1200,height=600)
    emp_frame.place(x=220,y=100)
    emp_name=Label(emp_frame,text="Manage Employee Details",font=("times new roman",19,"bold"),background="pink")
    emp_name.place(x=-3,y=0,relwidth=1)

root= Tk()

root.title("Python SQL Inventory System")
root.geometry("1270x668")
root.resizable(0,0)
root.config(background = "#f8e9d2")

icon=PhotoImage(file="inventory.png")
titlelabel=Label(root,text="Inventory Management Systems",image=icon,compound=LEFT,font=("times new roman",25),background="pink",fg="black")
titlelabel.place(x=0,y=0,relwidth=1)
logoutbutton.place(x=1150,y=20,)

sublabel=Label(root,text="Welcome User ",font=("times new roman",15),background="#88b89b",fg="white")
sublabel.place(x=0,y=70,relwidth=1)




sidelabel=Label(root,background="#f4a873")
sidelabel.place(x=0,y=100,width=220,height=600,relheight=1)




menulabel=Label(sidelabel,text="MENU",font=("times new roman",20,"bold"),background="#9c6b4e")
menulabel.pack(fill=X)

emp_image=PhotoImage(file="handshake.png")
emp_button= Button(sidelabel,text="   EMPLOYEE",font=("times new roman",18),image=emp_image,compound="left",anchor="w",command=employeeform)
emp_button.pack(fill=X)

sup_image=PhotoImage(file="distribution.png")
sup_button= Button(sidelabel,text="   SUPPLIERS",font=("times new roman",18),image=sup_image,compound="left",anchor="w")
sup_button.pack(fill=X)

cat_image=PhotoImage(file="options-lines.png")
cat_button= Button(sidelabel,text="   CATEGORIES",font=("times new roman",18),image=cat_image,compound="left",anchor="w")
cat_button.pack(fill=X)

pro_image=PhotoImage(file="briefing.png")
pro_button= Button(sidelabel,text="   PRODUCTS",font=("times new roman",18),image=pro_image,compound="left",anchor="w")
pro_button.pack(fill=X)

sales_image=PhotoImage(file="sales.png")
sales_button= Button(sidelabel,text="   SALES",font=("times new roman",18),image=sales_image,compound="left",anchor="w")
sales_button.pack(fill=X)

exit_image=PhotoImage(file="exit.png")
exit_button= Button(sidelabel,text="   EXIT",font=("times new roman",18),image=exit_image,compound="left",anchor="w")
exit_button.pack(fill=X)

emp_frame=Frame(root,background="#c43d5b")
emp_frame.place(x=350,y=150,width=300,height=200)

emp_icon=PhotoImage(file="team.png")
emp_iconlabel=Label(emp_frame,image=emp_icon,background="#c43d5b")
emp_iconlabel.pack(fill=X)

emp_label=Label(emp_frame,text="\nTOTAL EMPLOYEE",background="#c43d5b",font=("times new roman",17,"bold"),fg="white")
emp_label.pack(fill=X)

emp_count_label=Label(emp_frame,text="0",background="#c43d5b",font=("times new roman",30,"bold"),fg="white")
emp_count_label.pack(fill=X)

sup_frame=Frame(root,background="#c43d5b"
                )
sup_frame.place(x=800,y=150,width=300,height=200)

sup_icon=PhotoImage(file="delivery-courier.png")
sup_iconlabel=Label(sup_frame,image=sup_icon,background="#c43d5b")
sup_iconlabel.pack(fill=X)

sup_label=Label(sup_frame,text="\nTOTAL SUPPLIERS",background="#c43d5b",font=("times new roman",17,"bold"),fg="white")
sup_label.pack(fill=X)

sup_count_label=Label(sup_frame,text="0",background="#c43d5b",font=("times new roman",30,"bold"),fg="white")
sup_count_label.pack(fill=X)



totalcat_frame=Frame(root,background="#c43d5b")
totalcat_frame.place(x=280,y=400,width=300,height=200)

totalcat_icon=PhotoImage(file="categories.png")
totalcat_iconlabel=Label(totalcat_frame,image=totalcat_icon,background="#c43d5b")
totalcat_iconlabel.pack(fill=X)

totalcat_label=Label(totalcat_frame,text="\nTOTAL CATEGORIES",background="#c43d5b",font=("times new roman",17,"bold"),fg="white")
totalcat_label.pack(fill=X)

totalcat_count_label=Label(totalcat_frame,text="0",background="#c43d5b",font=("times new roman",30,"bold"),fg="white")
totalcat_count_label.pack(fill=X)

totalproducts_frame=Frame(root,background="#c43d5b")
totalproducts_frame.place(x=600,y=400,width=300,height=200)

totalproducts_icon=PhotoImage(file="portfolio.png")
totalproducts_iconlabel=Label(totalproducts_frame,image=totalproducts_icon,background="#c43d5b")
totalproducts_iconlabel.pack(fill=X)

totalproducts_label=Label(totalproducts_frame,text="\nTOTAL PRODUCTS",background="#c43d5b",font=("times new roman",17,"bold"),fg="white")
totalproducts_label.pack(fill=X)

totalproducts_count_label=Label(totalproducts_frame,text="0",background="#c43d5b",font=("times new roman",30,"bold"),fg="white")
totalproducts_count_label.pack(fill=X)


totalsales_frame=Frame(root,background="#c43d5b")
totalsales_frame.place(x=920,y=400,width=300,height=200)

totalsales_icon=PhotoImage(file="growth.png")
totalsales_iconlabel=Label(totalsales_frame,image=totalsales_icon,background="#c43d5b")
totalsales_iconlabel.pack(fill=X)

totalsales_label=Label(totalsales_frame,text="\nTOTAL SALES",background="#c43d5b",font=("times new roman",17,"bold"),fg="white")
totalsales_label.pack(fill=X)

totalsales_count_label=Label(totalsales_frame,text="0",background="#c43d5b",font=("times new roman",30,"bold"),fg="white")
totalsales_count_label.pack(fill=X)









root.mainloop()