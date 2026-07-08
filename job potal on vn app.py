from tkinter import *
from tkinter import messagebox
import mysql.connector

con=mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="pomato",
    database="student_db",
    use_pure=True
    )

cursor=con.cursor()

def save_data():
    sql="""
    INSERT INTO job
    (name,phoneno,age,address,country,job)
    VALUES(%s,%s,%s,%s,%s,%s)
    """
    values=(
        name.get(),
        phoneno.get(),
        age.get(),
        address.get(),
        country.get(),
        job.get(),
        )
    cursor.execute(sql,values)
    con.commit()

    messagebox.showinfo("Success","Data Saved Successfully")

    name.delete(0,END)
    phoneno.delete(0,END)
    age.delete(0,END)
    address.delete(0,END)
    country.delete(0,END)
    job.delete(0,END)

root=Tk()
root.title("JOB POTAL")
root.geometry("500x600")
root.configure(bg="lightblue")

Label(root,
      text="JOB POTAL",
      font=("Arial",18,"bold"),
      bg="lightblue",
      fg="darkblue").pack(pady=10)

Label(root,text="name",bg="lightblue").pack()
name=Entry(root,width=35)
name.pack()

Label(root,text="phoneno",bg="lightblue").pack()
phoneno=Entry(root,width=35)
phoneno.pack()

Label(root,text="age",bg="lightblue").pack()
age=Entry(root,width=35)
age.pack()

Label(root,text="address",bg="lightblue").pack()
address=Entry(root,width=35)
address.pack()

Label(root,text="country",bg="lightblue").pack()
country=Entry(root,width=35)
country.pack()

Label(root,text="job",bg="lightblue").pack()
job=Entry(root,width=35)
job.pack()

Button(root,
       text="Save Data",
       bg="green",
       fg="white",
       font=("Arial",12,"bold"),
       command=save_data).pack(pady=20)

root.mainloop()

con.close()



    
        
