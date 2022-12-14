from tkinter import *
import tkinter as tink
from PIL import ImageTk,Image
import json
from Admin_Interface import Admin

window = tink.Tk()
window.geometry("1300x700")
window.title("Airline Booking")

Adminbutton = tink.Button(text="Admin",font=("elephant",10,"italic"),height=2,width=10,command=Admin)
Adminbutton.pack(side="top")



window.mainloop()