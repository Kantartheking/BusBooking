from datetime import date
from tkinter import *
from tkinter import messagebox
import random
import sqlite3
root = Tk()
root.state('zoomed')
bus_logo = PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root, image=bus_logo).grid(row=0, column=5, columnspan=15)

Label(root, text="Online Bus Booking System", bg="Light Blue",
      fg="Red", font="Arial 20").grid(row=1, column=5, columnspan=15)
Label(root, text="Enter Journey Details", bg="Light Green",
      font="Arial 10").grid(row=2, column=5, pady=15, columnspan=15)


Label(root, text='To').grid(row=3, column=3)
to = Entry(root)
to.grid(row=3, column=4, pady=20)

Label(root, text='From').grid(row=3, column=5)
fro = Entry(root)
fro.grid(row=3, column=6, pady=20)

Label(root, text='Journey Date').grid(row=3, column=7)
journey_date = Entry(root)
journey_date.grid(row=3, column=8)


def show():
    Button(root, text="Proceed to Book",
           command=proceed).grid(row=5, column=10)


def show_bus():
    if to.get() == "" and fro.get() == "" and journey_date.get() == "":
        messagebox.showerror("Error", "<Please fill all the journey details>")
    elif to.get() == "" and fro.get() == "":

        messagebox.showerror("Error", "<Please fill the field <To and From>")
    elif fro.get() == "" and journey_date.get() == "":

        messagebox.showerror(
            "Error", "Please fill the field <From and Journey Date>")
    elif journey_date.get() == "" and to.get() == "":

        messagebox.showerror(
            "Error", "Please fill the field <To and Journey Date>")
    elif to.get() == "":

        messagebox.showerror("Error", "Please fill the fieldd <To>")
    elif fro.get() == "":
        messagebox.showerror("Error", "Please fill the field <From>")

    elif journey_date.get() == "":
        messagebox.showerror("Error ", "Please enter the field <Journey Date>")
    else:
        Label(root, text="Select Bus").grid(row=4, column=4)
        Label(root, text="Operator").grid(row=4, column=5)
        Label(root, text="Bus Type").grid(row=4, column=6)
        Label(root, text="Available").grid(row=4, column=7)
        Label(root, text="Capacity").grid(row=4, column=8)
        Label(root, text="Fare").grid(row=4, column=9)

        con = sqlite3.Connection("Bus_database")
        cur = con.cursor()

        cur.execute("select o.Name,b.Bus_type,d.Seat_available,b.Capacity,b.Fare ,b.B_Id from Operator_details as o,Bus_details as b,Running_details as d ,Route_details as r ,Route_details as e where o.Op_Id=b.Op_Id and r.S_Id>e.S_Id and b.B_Id=d.B_Id and r.R_Id=b.R_Id and e.R_Id=b.R_Id and r.Sname=? and e.Sname=?  and d.Date=?", (fro.get(), to.get(), journey_date.get(),))

        name = cur.fetchall()
        global b_id
        b_id = IntVar()
        n = 5
        for i in name:
            Radiobutton(root, text="Book Now", variable=b_id,
                        value=i[5]).grid(row=n, column=4)
            Label(root, text=i[0]).grid(row=n, column=5)
            Label(root, text=i[1]).grid(row=n, column=6)
            Label(root, text=i[2]).grid(row=n, column=7)
            Label(root, text=i[3]).grid(row=n, column=8)
            Label(root, text=i[4]).grid(row=n, column=9)
            n = n+1
        show()


Button(root, text="Show Bus", command=show_bus).grid(row=3, column=9, pady=20)


def proceed():

    Label(root, text='Fill Passenger Details to book bus ticket', font='Arial 18 bold ',
          fg='red', bg='light blue').grid(row=20, column=6, pady=20, columnspan=15)

    Label(root, text="Name").grid(row=22, column=3)
    name = Entry(root)
    name.grid(row=22, column=4)

    Label(root, text="Gender").grid(row=22, column=5)
    gender_type = StringVar()
    gender_option = ["Male", "Female"]
    gender_menu = OptionMenu(
        root, gender_type, *gender_option).grid(row=22, column=6)

    Label(root, text="No of Seats").grid(row=22, column=7)
    no_of_seats = Entry(root)
    no_of_seats.grid(row=22, column=8)

    Label(root, text="Mobile No").grid(row=22, column=9)
    mobile_number = Entry(root)
    mobile_number.grid(row=22, column=10)
    print(mobile_number)

    Label(root, text="Age").grid(row=22, column=11)
    age = Entry(root)
    age.grid(row=22, column=12)

    Button(root, text="Book Seat", command=bus_ticket).grid(
        row=22, column=13, padx=5)

    con = sqlite3.Connection("Bus_database")
    cur = con.cursor()

    m = mobile_number.get()
    n = name.get()
    ns = no_of_seats.get()
    g = gender_type.get()
    a = age.get()
    b = b_id.get()
    d = date.today()
    j = journey_date.get()
    o = random.randint(1, 100)
    f = fro.get()
    # print(m)
    # print(n)
    # print(ns)
    # print(g)
    # print(a)
    # print(b)
    # print(d)
    # print(j)
    # print(f)
    # print(o)

    if mobile_number.get() != "" and name.get() != "" and no_of_seats.get() != "" and gender_type.get() != "" and age.get() != "":
        #     cur.execute("insert into Booking_history values('"+mobile_number.get() + "','"+name.get()+"','"+no_of_seats .get()+"','"+gender_type.get() +
        #                 "','"+age.get()+"','"+b_id.get()+"','"+date.today()+"','"+journey_date.get()+"','"+random.randint(1, 100)+"','"+fro.get()+"')")
        cur.execute('''insert into Booking_history(Phone,Passenger_name ,No_of_passenger,Gender,Age,B_Id,Date,Journey_date,Booking_ref,Boarding_station)values(?,?,?,?,?,?,?,?,?,?)''', (m, n, ns, g, a, b, d, j, o, f))
        con.commit()

        cur.execute("update Running_details set r.Seat_available=r.Seat_available-No_of_passenger from Running_details as r ,Booking_history as b where b.B_Id=r.B_Id and b.Journey_date=r.Date")
        con.commit()
        con.close()
    else:
        messagebox.showerror("","Please fill all the details")


def bus_ticket():
    check = messagebox.askyesno(
        "Booking Confirmation", "Click Yes to book ticket")
    if check:
        root.destroy()
        import bus_ticket
    else:
        messagebox.showerror("", "Booking Failed")


def home():
    root.destroy()
    import booking_details


home_logo = PhotoImage(file=".\\images\\home.png")
Button(root, fg='black', bg='light green', image=home_logo,
       command=home).grid(row=3, column=10)


root.mainloop()
