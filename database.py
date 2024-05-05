import sqlite3
con=sqlite3.connect("Bus_database")
cur=con.cursor()
# cur.execute("CREATE TABLE Operator_details (Op_Id INTEGER PRIMARY KEY ,Name varchar(100) NOT NULL,Address TEXT NOT NULL,Email varchar(64),Phone INTEGER)");
#cur.execute("drop table Bus_details")
#cur.execute("drop table Running_details")
cur.execute("CREATE TABLE Bus_details(B_Id INTEGER PRIMARY KEY,Bus_type char(5),Capacity INTEGER,Fare INTEGER,R_Id INTEGER, Op_Id INTEGER ,CONSTRAINT fk_OP_Id  FOREIGN KEY (Op_Id)REFERENCES Operator_details(Op_Id))");
cur.execute("CREATE TABLE Running_details(B_Id INTEGER,Date DATE,Seat_available INTEGER,PRIMARY KEY(B_Id,Date))");
# cur.execute("CREATE TABLE Route_details(R_Id INTEGER,Sname TEXT NOT NULL,S_Id INTEGER ,PRIMARY KEY(R_Id,S_Id))");
# cur.execute("CREATE TABLE Booking_history(Phone INTEGER PRIMARY KEY,Passenger_name TEXT,No_of_passenger INTEGER,B_Id INTEGER,Boarding_station TEXT,Departure_station TEXT,Journey_date DATE)")
# # # cur.execute("INSERT INTO Operator_details(Op_Id,Name,Address,Email,Phone)VALUES(1,)")

#cur.execute("CREATE TABLE Booking_history(Passenger_name TEXT not null,Gender varchar(10) ,No_of_passenger integer,Phone integer PRIMARY KEY,Age integer, B_Id INTEGER NOT NULL,Date Date NOT NULL,Journey_date DATE NOT NULL,Booking_ref integer,Boarding_station Text)")
#cur.execute("alter table Booking_history add column Booking_ref INTEGER")
#cur.execute("insert into Booking_history(Passenger_name ,Gender,No_of_passenger ,Phone,Age , B_Id,Date,Journey_date,Booking_ref,Boarding_station) values('Aryan','Male',2,8299402300,20,2,'2022-10-29','2022-20-29',21,'Guna')")
#cur.execute("drop table Booking_history")
con.commit()
