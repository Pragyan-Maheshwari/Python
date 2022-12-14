from tkinter import *
import tkinter as Adtink
import tkinter.ttk as ttk
import json

def Admin():
    adwin = Adtink.Tk()
    adwin.title("Admin")
    adwin.geometry("1300x700")

    #Check Flights
    def flights():
        flight = Adtink.Tk()
        flight.title("Flights")
        flight.geometry("1300x700")
        flight.configure(bg="green")
        
        with open("Final Project\Flights.json") as file:
            flightsdata = json.load(file)


        Flightstable = ttk.Treeview(flight, show="headings", columns=("Sno.","From","Destination","Boarding Time","Arival Time","Seats Left"))
        
        Flightstable.heading("#1", text="Sno.")
        Flightstable.heading("#2", text="From")
        Flightstable.heading("#3", text="Destination")
        Flightstable.heading("#4", text="Boarding Time")
        Flightstable.heading("#5", text="Arival Time")
        Flightstable.heading("#6", text="Seats Left")
        Flightstable.grid()

        for row in flightsdata:
            Flightstable.insert("","end",values=(row["Sno."],row["From"],row["Destination"],row["Boarding Time"],row["Arival Time"],row["Seats Left"]))

        flight.mainloop()

    flightcheck = Adtink.Button(text="Check Flights",font=("elephant",10,"italic"),height=2,width=10,command=flights)
    flightcheck.pack(side="top")
    
    #Check Passangers
    def passangers():
        passanger = Adtink.Tk()
        passanger.title("Passangers")
        passanger.geometry("1300x700")
        passanger.configure(bg="green")


        with open("Final Project\Passangers.json") as file:
            passangerdata = json.load(file)


        PassangerTable = ttk.Treeview(passanger, show="headings", columns=("Serial No.","Name","Flight","Age","Gender"))
                
        PassangerTable.heading("#1", text="Serial No.")
        PassangerTable.heading("#2", text="Name")
        PassangerTable.heading("#3", text="Flight")
        PassangerTable.heading("#4", text="Age")
        PassangerTable.heading("#5", text="Gender")
        PassangerTable.grid()

        for row in passangerdata:
            PassangerTable.insert("","end",values=(row["Serial No."],row["Name"],row["Flight"],row["Age"],row["Gender"]))

        passanger.mainloop()


    passangercheck = Adtink.Button(text="Check Passangers",font=("elephant",10,"italic"),height=2,width=10,command=passangers)
    passangercheck.pack(side="top")

    #need to place add flight

    adwin.mainloop()