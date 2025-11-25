import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- DATABASE ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sumit@2006",  
        database="hospital"
    )


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("1150x750")
root.config(bg="#f0f8ff")

# ==============================================================#
#                      PATIENT SECTION                          #
# ==============================================================#
p_id = ""
p_name = tk.StringVar()
p_age = tk.StringVar()
p_gender = tk.StringVar()
p_disease = tk.StringVar()
p_phone = tk.StringVar()


def add_patient():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(
            "INSERT INTO patient(name, age, gender, disease, phone) VALUES (%s,%s,%s,%s,%s)",
            (p_name.get(), p_age.get(), p_gender.get(), p_disease.get(), p_phone.get())
        )
        con.commit()
        con.close()
        fetch_patient()
        clear_patient_fields()
        messagebox.showinfo("Success", "Patient added successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def fetch_patient():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    patient_table.delete(*patient_table.get_children())
    for row in rows:
        patient_table.insert("", tk.END, values=row)
    con.close()


def get_patient(event):
    global p_id
    selected = patient_table.focus()
    data = patient_table.item(selected)["values"]
    if data:
        p_id = data[0]
        p_name.set(data[1])
        p_age.set(data[2])
        p_gender.set(data[3])
        p_disease.set(data[4])
        p_phone.set(data[5])


def update_patient():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute(
            "UPDATE patient SET name=%s, age=%s, gender=%s, disease=%s, phone=%s WHERE id=%s",
            (p_name.get(), p_age.get(), p_gender.get(), p_disease.get(), p_phone.get(), p_id)
        )
        con.commit()
        con.close()
        fetch_patient()
        clear_patient_fields()
        messagebox.showinfo("Updated", "Patient updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_patient():
    try:
        con = connect_db()
        cur = con.cursor()
        cur.execute("DELETE FROM patient WHERE id=%s", (p_id,))
        con.commit()
        con.close()
        fetch_patient()
        clear_patient_fields()
        messagebox.showinfo("Deleted", "Patient deleted!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def clear_patient_fields():
    global p_id
    p_id = ""
    p_name.set("")
    p_age.set("")
    p_gender.set("")
    p_disease.set("")
    p_phone.set("")


tk.Label(root, text="PATIENT DETAILS", bg="#f0f8ff", fg="blue", font=("Arial", 17, "bold")).place(x=20, y=10)

tk.Label(root, text="Name").place(x=20, y=50)
tk.Entry(root, textvariable=p_name).place(x=140, y=50)

tk.Label(root, text="Age").place(x=20, y=80)
tk.Entry(root, textvariable=p_age).place(x=140, y=80)

tk.Label(root, text="Gender").place(x=20, y=110)
ttk.Combobox(root, textvariable=p_gender, values=["Male", "Female"]).place(x=140, y=110)

tk.Label(root, text="Disease").place(x=20, y=140)
tk.Entry(root, textvariable=p_disease).place(x=140, y=140)

tk.Label(root, text="Phone").place(x=20, y=170)
tk.Entry(root, textvariable=p_phone).place(x=140, y=170)

tk.Button(root, text="Add", command=add_patient, bg="lightgreen").place(x=20, y=210)
tk.Button(root, text="Update", command=update_patient, bg="yellow").place(x=90, y=210)
tk.Button(root, text="Delete", command=delete_patient, bg="red").place(x=170, y=210)
tk.Button(root, text="Clear", command=clear_patient_fields, bg="lightblue").place(x=250, y=210)

patient_table = ttk.Treeview(root, columns=("ID", "Name", "Age", "Gender", "Disease", "Phone"), show='headings')
for col in ("ID", "Name", "Age", "Gender", "Disease", "Phone"):
    patient_table.heading(col, text=col)
patient_table.place(x=350, y=30, width=780, height=170)

patient_table.bind("<ButtonRelease-1>", get_patient)
fetch_patient()


# ==============================================================#
#                      DOCTOR SECTION                           #
# ==============================================================#
d_id = ""
d_name = tk.StringVar()
d_spec = tk.StringVar()
d_phone = tk.StringVar()


def add_doctor():
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO doctor(name, specialization, phone) VALUES (%s,%s,%s)",
                (d_name.get(), d_spec.get(), d_phone.get()))
    con.commit()
    con.close()
    fetch_doctor()
    clear_doctor()


def fetch_doctor():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM doctor")
    rows = cur.fetchall()
    doctor_table.delete(*doctor_table.get_children())
    for row in rows:
        doctor_table.insert("", tk.END, values=row)
    con.close()


def get_doctor(event):
    global d_id
    selected = doctor_table.focus()
    data = doctor_table.item(selected)["values"]
    if data:
        d_id = data[0]
        d_name.set(data[1])
        d_spec.set(data[2])
        d_phone.set(data[3])


def update_doctor():
    con = connect_db()
    cur = con.cursor()
    cur.execute("UPDATE doctor SET name=%s, specialization=%s, phone=%s WHERE id=%s",
                (d_name.get(), d_spec.get(), d_phone.get(), d_id))
    con.commit()
    con.close()
    fetch_doctor()
    clear_doctor()


def delete_doctor():
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM doctor WHERE id=%s", (d_id,))
    con.commit()
    con.close()
    fetch_doctor()
    clear_doctor()


def clear_doctor():
    global d_id
    d_id = ""
    d_name.set("")
    d_spec.set("")
    d_phone.set("")


tk.Label(root, text="DOCTOR DETAILS", bg="#f0f8ff", fg="green", font=("Arial", 17, "bold")).place(x=20, y=270)

tk.Label(root, text="Name").place(x=20, y=310)
tk.Entry(root, textvariable=d_name).place(x=140, y=310)

tk.Label(root, text="Spec.").place(x=20, y=340)
tk.Entry(root, textvariable=d_spec).place(x=140, y=340)

tk.Label(root, text="Phone").place(x=20, y=370)
tk.Entry(root, textvariable=d_phone).place(x=140, y=370)

tk.Button(root, text="Add", command=add_doctor, bg="lightgreen").place(x=20, y=410)
tk.Button(root, text="Update", command=update_doctor, bg="yellow").place(x=90, y=410)
tk.Button(root, text="Delete", command=delete_doctor, bg="red").place(x=170, y=410)
tk.Button(root, text="Clear", command=clear_doctor, bg="lightblue").place(x=250, y=410)

doctor_table = ttk.Treeview(root, columns=("ID", "Name", "Spec", "Phone"), show='headings')
for col in ("ID", "Name", "Spec", "Phone"):
    doctor_table.heading(col, text=col)
doctor_table.place(x=350, y=260, width=780, height=150)

doctor_table.bind("<ButtonRelease-1>", get_doctor)
fetch_doctor()


# ==============================================================#
#                      EMPLOYEE SECTION                         #
# ==============================================================#
e_id = ""
e_name = tk.StringVar()
e_role = tk.StringVar()
e_salary = tk.StringVar()
e_phone = tk.StringVar()


def add_employee():
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO employee(name, role, salary, phone) VALUES (%s,%s,%s,%s)",
                (e_name.get(), e_role.get(), e_salary.get(), e_phone.get()))
    con.commit()
    con.close()
    fetch_employee()
    clear_employee()


def fetch_employee():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    employee_table.delete(*employee_table.get_children())
    for row in rows:
        employee_table.insert("", tk.END, values=row)
    con.close()


def get_employee(event):
    global e_id
    selected = employee_table.focus()
    data = employee_table.item(selected)["values"]
    if data:
        e_id = data[0]
        e_name.set(data[1])
        e_role.set(data[2])
        e_salary.set(data[3])
        e_phone.set(data[4])


def update_employee():
    con = connect_db()
    cur = con.cursor()
    cur.execute("UPDATE employee SET name=%s, role=%s, salary=%s, phone=%s WHERE id=%s",
                (e_name.get(), e_role.get(), e_salary.get(), e_phone.get(), e_id))
    con.commit()
    con.close()
    fetch_employee()
    clear_employee()


def delete_employee():
    con = connect_db()
    cur = con.cursor()
    cur.execute("DELETE FROM employee WHERE id=%s", (e_id,))
    con.commit()
    con.close()
    fetch_employee()
    clear_employee()


def clear_employee():
    global e_id
    e_id = ""
    e_name.set("")
    e_role.set("")
    e_salary.set("")
    e_phone.set("")


tk.Label(root, text="EMPLOYEE DETAILS", bg="#f0f8ff", fg="maroon", font=("Arial", 17, "bold")).place(x=20, y=510)

tk.Label(root, text="Name").place(x=20, y=550)
tk.Entry(root, textvariable=e_name).place(x=140, y=550)

tk.Label(root, text="Role").place(x=20, y=580)
tk.Entry(root, textvariable=e_role).place(x=140, y=580)

tk.Label(root, text="Salary").place(x=20, y=610)
tk.Entry(root, textvariable=e_salary).place(x=140, y=610)

tk.Label(root, text="Phone").place(x=20, y=640)
tk.Entry(root, textvariable=e_phone).place(x=140, y=640)

tk.Button(root, text="Add", command=add_employee, bg="lightgreen").place(x=20, y=680)
tk.Button(root, text="Update", command=update_employee, bg="yellow").place(x=90, y=680)
tk.Button(root, text="Delete", command=delete_employee, bg="red").place(x=170, y=680)
tk.Button(root, text="Clear", command=clear_employee, bg="lightblue").place(x=250, y=680)

employee_table = ttk.Treeview(root, columns=("ID", "Name", "Role", "Salary", "Phone"), show='headings')
for col in ("ID", "Name", "Role", "Salary", "Phone"):
    employee_table.heading(col, text=col)
employee_table.place(x=350, y=500, width=780, height=180)

employee_table.bind("<ButtonRelease-1>", get_employee)
fetch_employee()

root.mainloop()