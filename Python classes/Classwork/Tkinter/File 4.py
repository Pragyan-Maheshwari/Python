from email.mime import image
import tkinter as tink
from tkinter.ttk import Label, Button
from PIL import ImageTk,Image
from turtle import bgcolor

window = tink.Tk()
window.geometry("700x700")

def ClickExitButton():
    label = tink.Label(text = "Azadi Ka Amrit Mahotasv Mubarak",font = ("Elephant",30,"bold"))
    label.pack(side="top")
    
    frame=tink.Frame(window,width= 50000,height=50000)
    frame.pack()
    frame.place(anchor="s",relx=10,rely=10)
    
    img = ImageTk.PhotoImage(Image.open("Python classes//Flag.jpeg"))
    mylable = Label(frame,image = img)
    mylable.pack()

exitButton = Button(text = ":)",command = ClickExitButton)
exitButton.pack(side = "top")

window.mainloop()