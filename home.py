from tkinter import *
root=Tk()
root.state('zoomed')
bus_logo=PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root,image=bus_logo).grid(row=0,column=1,padx=600)
Label(root,text="Online Bus Booking System",bg="light blue",fg="Red",font=50).grid(row=1,column=1)
Label(root,text="Name : Aryan Tripathi",fg="Blue").grid(row=2,column=1,pady=30)
Label(root,text="Er : 211B066",fg="Blue").grid(row=3,column=1)
Label(root,text="Mobile : 8299402300",fg="Blue").grid(row=4,column=1,pady=30)
Label(root,text="Sumbmitted to : Dr. Mahesh Kumar",bg="Light Blue",fg="Red",font=10).grid(row=5,column=1)
Label(root,text="Project Based Learning",fg="Red").grid(row=6,column=1)

def booking_details(k=0):
    root.destroy()
    import booking_details

root.bind("<KeyPress>",booking_details)


root.mainloop()

