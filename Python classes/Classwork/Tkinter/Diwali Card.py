from tkinter import *
from email.mime import image
import tkinter as tink
from tkinter.ttk import Label
from PIL import ImageTk,Image
window = tink.Tk()
window.title("Happy Diwali")
window.minsize(width=600, height=600)
window.geometry("1300x700")

lable = tink.Label(text = "Happy Diwali",font = ("Elephant",100,"bold"),bg='Red')
lable.pack(side="top")

frame=tink.Frame(window,width= 50000,height=50000)
frame.pack()
frame.place(anchor="s",relx=0.5,rely=0.8)
img = ImageTk.PhotoImage(Image.open("Python classes/Classwork/Tkinter/Diwali1.jpeg"))
mylable = Label(frame,image = img)
mylable.pack()

frame2=tink.Frame(window,width= 50000,height=50000)
frame2.pack()
frame2.place(anchor="s",relx=0.5,rely=0.6)
img2 = ImageTk.PhotoImage(Image.open("Python classes/Classwork/Tkinter/Diwali2.jpeg"))
mylable2 = Label(frame2,image = img2)
mylable2.pack()

window.mainloop()