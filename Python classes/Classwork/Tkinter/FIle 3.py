from email.mime import image
import tkinter as tink
from tkinter.ttk import Label
from PIL import ImageTk,Image
window = tink.Tk()
window.title("Azadi Ka Amrit Mahotasv")
window.minsize(width=600, height=600)
window.geometry("600x600")

label = tink.Label(text = "Azadi Ka Amrit Mahotasv Mubarak",font = ("Elephant",30,"bold"))
label.pack(side="top")

frame=tink.Frame(window,width= 50000,height=50000)
frame.pack()
frame.place(anchor="s",relx=0.5,rely=0.8)
img = ImageTk.PhotoImage(Image.open("Python classes//Flag.jpeg"))
mylable = Label(frame,image = img)
mylable.pack()

window.mainloop()