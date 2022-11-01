from email.mime import image
import tkinter as tink
from tkinter.ttk import Label, Button
from PIL import ImageTk,Image
from turtle import bgcolor
from tkinter import *

window = tink.Tk()
window.geometry("800x800")
window.configure(bg = 'blue')

Fillbox1 = tink.Entry(window,bg='orange',background="red",)
Fillbox1.pack()

def maxblow():
    x = Fillbox1.get()
    label1 = tink.Label(text=x,bg='green')
    label1.pack(side='top')

button1 = Button(text= 'SuS ඞ SuS',height="3",width="6",command=maxblow)
button1.pack(side="top")

window.mainloop()