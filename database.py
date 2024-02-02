from tkinter import *
import sqlite3
root=Tk()
lbl=Label(root,text='employee management system',font=('arial bold',50))
lbl.place(x=200,y=0)
root.geometry('1500x1500')
root.resizable(0,0)
conn=sqlite3.connect('database.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS student(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        uname           TEXT,
        adr             TEXT,
        rl              TEXT,
        slr             INT
               
)''')

conn.commit()
conn.close()

def add():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('INSERT INTO student(uname,adr,rl,slr) VALUES(?,?,?,?)',
              (username.get(),address.get(),role.get(),salary.get()))
    conn.commit()
    conn.close()
    username.delete(0,END)
    address.delete(0,END)
    role.delete(0,END)
    salary.delete(0,END)

def retrieve():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('SELECT * FROM student')
    records=c.fetchall()##fetchmany(3)##to display three records
    # print(records)
    print_record=""
    for record in records :
        print_record+=str(record[0])+ str(record[1])+str (record[4])+'\n'
    
    label_retrieve=Label(text=print_record)
    label_retrieve.place(x=10,y=470)
    conn.close()  



def delete ():
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('DELETE FROM student WHERE ID ='+detetebox.get())
    conn.commit()
    conn.close()
    detetebox.delete(0,END)
    retrieve()

def edit():
    global editor
    editor=Tk()
    editor.title('update data')
    editor.geometry('300x400')

    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    record_id=update_box.get()
    c.execute('SELECT * FROM student WHERE ID =?',(record_id,))
    records=c.fetchall()

    global username_editor
    global address_editor
    global role_editor
    global salary_editor
    
    username_editor=Entry(editor,width=30)
    username_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=1,column=1)

    role_editor=Entry(editor,width=30)
    role_editor.grid(row=2,column=1)

    salary_editor=Entry(editor,width=30)
    salary_editor.grid(row=3,column=1)

    #create text box labels
    username_label=Label(editor,text='username')
    username_label.grid(row=0,column=0,pady=(10,0))

    address_label=Label(editor,text='address')
    address_label.grid(row=1,column=0)

    role_label=Label(editor,text='role')
    role_label.grid(row=2,column=0)

    salary_label=Label(editor,text='salary')
    salary_label.grid(row=3,column=0)


    for record in records:
        username_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        role_editor.insert(0,record[3])
        salary_editor.insert(0,record[4])
    update_box.delete(0,END)
    ##create a save button
    edit_btn=Button(editor,text='save',command=lambda:update(record_id))
    edit_btn.grid(row=7,column=0,columnspan=2,pady=10,ipadx=125)



def update(record_id):
    conn=sqlite3.connect('database.db')
    c=conn.cursor()
    c.execute('''
              UPDATE student SET
              uname=:u,
              adr=:a,
              rl=:r,
              slr=:s
                WHERE ID =:id''',
                {
                    'u':username_editor.get(),
                    'a':address_editor.get(),
                    'r':role_editor.get(),
                    's':salary_editor.get(),
                    'id':record_id
                }
                )
    conn.commit()
    conn.close()
    #destroying all the data and closing wiindow
    editor.destroy()





label_username=Label(root,text='username',font=('Arial Bold',20))
label_username.place(x=0,y=90)

label_address=Label(root,text='address',font=('Arial Bold',20))
label_address.place(x=0,y=140)

label_role=Label(root,text='role',font=('Arial Bold',20))
label_role.place(x=0,y=190)


label_salary=Label(root,text='salary',font=('Arial Bold',20))
label_salary.place(x=0,y=240)


label_delete=Label(root,text='delete  record',font=('Arial Bold',20))
label_delete.place(x=0,y=370)

username=Entry(width=30)
username.place(x=170,y=100,height=30)

address=Entry(root,width=30)
address.place(x=170,y=150,height=30)

role=Entry(width=30)
role.place(x=170,y=200,height=30)

salary=Entry(width=30)
salary.place(x=170,y=250,height=30)



btn_add=Button(root,text='add',font=("Arial bold",20),command=add)
btn_add.place(x=0,y=300)

btn_retrieve=Button(root,text='retrieve',font=("Arial bold",20),command=retrieve)
btn_retrieve.place(x=100,y=300)

btn_delete=Button(root,text='delete',font=("Arial bold",20),command=delete)
btn_delete.place(x=370,y=380)

detetebox=Entry(width=25)
detetebox.place(x=210,y=370,height=30)

btn_update=Button(text='update ',font=('Ariel Bold ',20),width=5,command=edit)
btn_update.place(x=380,y=440)

update_box=Entry(width=25)
update_box.place(x=210,y=460,height=30 )

update_label=Label(text='update record',font=('Ariel Bold',20))
update_label.place(x=10,y=440)



root.mainloop()
