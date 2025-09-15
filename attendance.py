from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from student_attendancedb import *
from tkcalendar import DateEntry

krish=Tk()
krish.title("student_attendance")
krish.geometry("1366x768")

addstudent=LabelFrame(krish,text="Add studen ",font=("Arial",20,"bold"),fg="orange")
addstudent.place(x=10,y=10,width=350,height=200)
def addstudents():
    if stdides.get()=="" and stdnamee.get()=="":
        messagebox.showwarning("msg","⚠️Fill all the fields")
    else:
             
        studentid=stdides.get().strip()
        studentname=stdnamee.get().strip()
        student_details=(f"{ studentid} - { studentname}")
        lstbox.insert(END, student_details)
        datas=attendance("attendance_record.db")
        datas.insert(studentid, studentname)
        stdides.delete(0,END)
        stdnamee.delete(0,END)
    
    
    
def markattendance():
    if stdidea.get()=="" and attendance_status.get()=="" and date_le.get()=="":
        messagebox.showwarning("msg","⚠️Fill all the fields")
    else:
        studenid=stdidea.get()
        status=attendance_status.get()
        date=date_le.get()
        datas=attendance("attendance_record.db")
        datas.attendance_insert( studenid,status,date)
        stdidea.delete(0,END)
        attendance_status.delete(0,END)
        date_le.delete(0,END)
def show_attendance_detail():
    ids=stdi.get()
    datas=attendance("attendance_record.db")
    value=datas.fetch(ids)
    for i in value:
        mytree.insert("","end",values=(i[3],i[2]))
    datas=attendance("attendance_record.db")
    val=datas.showstddetail(ids)
    for i in val:
        show_detai.config(text=f"Attendance will show here  {i[1]} - { i[2]}")
     
            
stdid=Label(addstudent,text="Student id",font=("times",10,"bold"))
stdid.grid(row=0,column=0)
stdides=Entry(addstudent,font=("times",10,"bold"))
stdides.grid(row=0,column=1,padx=10)

stdname=Label(addstudent,text="Student Name",font=("times",10,"bold"))
stdname.grid(row=1,column=0)
stdnamee=Entry(addstudent,font=("times",10,"bold"))
stdnamee.grid(row=1,column=1,pady=20,padx=10)

addbtn=Button(addstudent,text="Add student",font=("times",10,"bold"),command=addstudents,bg="green",fg="white")
addbtn.grid(columnspan=3)


mark_attendance=LabelFrame(krish,text="Mark Attendance",font=("Arial",20,"bold"),fg="orange")
mark_attendance.place(x=10,y=220,width=350,height=200)

stdid=Label(mark_attendance,text="Student ID",font=("Arial",10,"bold"))
stdid.grid(row=0,column=0,padx=10)

stdidea=Entry(mark_attendance,font=("Arial",10,"bold"))
stdidea.grid(row=0,column=1,padx=10)

attendance_statusl=Label(mark_attendance,text="Status",font=("Arial",10,"bold"))
attendance_statusl.grid(row=1,column=0,padx=10)

attendance_status=ttk.Combobox(mark_attendance,font=("Arial",8,"bold"),values=["present","absent","late"])

attendance_status.grid(row=1,column=1,pady=10,padx=10)

date_l=Label(mark_attendance,text="date(yyyy-mm-dd)",font=("Arial",10,"bold"))

date_l.grid(row=2,column=0,padx=10)


date_le=DateEntry(mark_attendance,font=("Arial",8,"bold") ,date_pattern='yyyy-mm-dd')

date_le
date_le.grid(row=2,column=1,pady=10,padx=10)

addbtn=Button(mark_attendance,text="Mark Attendance",font=("times",10,"bold"),command=markattendance,bg="green",fg="white")
addbtn.grid(columnspan=4)

stdlist=LabelFrame(krish,text="Studen List",font=("Arial",20,"bold"),fg="orange")
stdlist.place(x=10,y=420,width=350,height=300)

stdl=Label(stdlist,text="Student list",font=("Arial",10,"bold"))
stdl.grid(row=0,column=0)

lstfrm=Frame(stdlist)
lstfrm.grid(row=1,column=1,columnspan=2,sticky="nsew")

lstscrol=ttk.Scrollbar(lstfrm,orient="vertical")
lstscrol.pack(side=RIGHT,fill=Y)

lstbox= Listbox(lstfrm,width=30,yscrollcommand=lstscrol.set)
lstbox.pack(side="left",fill=BOTH,expand=True)

lstscrol.configure(command=lstbox.yview)



    


attendance_tree=LabelFrame(krish,text="View attendance",font=("Arial",20,"bold"),fg="orange")
attendance_tree.place(x=500,y=10,width=500,height=500)

stdid=Label(attendance_tree,text="Student id",font=("times",10,"bold"))
stdid.grid(row=0,column=0,padx=50)
stdi=Entry(attendance_tree,font=("times",10,"bold"))
stdi.grid(row=0,column=1,padx=160)


show_detai=Label(attendance_tree,text="Show  Attendance Details")
show_detai.grid(columnspan=1,pady=20)


treefrm=Frame(attendance_tree)
treefrm.place(x=10, y=100, width=480, height=300)


trscr=ttk.Scrollbar(treefrm,orient="vertical")
trscr.pack(side=RIGHT,fill="y")


mytree=ttk.Treeview(treefrm,yscrollcommand=trscr.set)
mytree["column"]=("date","status")
mytree.column("#0",width=0,stretch=NO)
mytree.column("#1",width=150)
mytree.column("#2",width=150)

mytree.heading("#0",text="")
mytree.heading("#1",text="Date")
mytree.heading("#2",text="Status")

mytree.pack(side=LEFT, fill=BOTH, expand=True)
trscr.configure(command=mytree.yview)

datas=attendance("attendance_record.db")
val=datas.studelist()
for i in val:
   
    
    student_details=(f"{ i[1]} - { i[2]}")
    lstbox.insert(END, student_details)


show_btn=Button(attendance_tree,text="Attendance will show here",command=show_attendance_detail,bg="green",fg="white")
show_btn.place(x=10,y=400)

krish.mainloop()

