from tkinter import *
a= Tk ()
import sqlite3

a.title('registration')
a.iconbitmap('registration.ico')

a.maxsize(width=600,height=800)
a.minsize(width=400,height=500)
# a.config(bg='green')
# b=PhotoImage (file='apartment.jpg')

reg=Label(text='REGISTER HERE',font=('arial',15,'bold')).place(x=100,y=20)
First=Label(text="First Name").place(x=50,y=80)
last=Label(text='Last Name').place(x=50,y=110)
email=Label(text='Email').place(x=75,y=140)
dob=Label(text='Date of Birth').place(x=40,y=170)
address=Label(text='Address').place(x=60,y=200)
ask=Label(text='Already have an account? ').place(x=90,y=360)
pw=Label(text='Password').place(x=57,y=230)
pw1=Label(text='Confirm Password').place(x=10,y=260)

register=Button(text='Register').place(x=120,y=330)


def register():
    a.destroy()
    import project

btn=Button(text='login',command=register).place(x=230,y=355)

first1=Entry(a).place(x=130,y=80)
last1=Entry(a).place(x=130,y=110)
email1=Entry(a).place(x=130,y=140)
dob1=Entry(a).place(x=130,y=170)
address1=Entry(a).place(x=130,y=200)
pw1=Entry(a).place(x=130,y=230)
pw11=Entry(a).place(x=130,y=260)
a.mainloop ()