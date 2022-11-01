from email.mime import image
import tkinter as tink
from tkinter.ttk import Label, Button
from PIL import ImageTk,Image
from turtle import bgcolor
from tkinter import *

window = tink.Tk()
window.geometry("700x700")
window.configure(bg='blue')

entry = tink.Entry(window,bg="orange")
entry.pack()

def ClickExitButton():
    x = entry.get()
    label = tink.Label(text = x,font = ("Elephant",30,"bold"),bg='red')
    label.pack(side="top")

exitButton = Button(text = "Printer",command = ClickExitButton, bg='blue', height = 2, width = 10)
exitButton.pack(side = "top")


window.mainloop()