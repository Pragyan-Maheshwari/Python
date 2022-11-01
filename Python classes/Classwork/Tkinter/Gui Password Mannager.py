from email.mime import image
import tkinter as tink
from tkinter.ttk import Label, Button
from PIL import ImageTk,Image
from turtle import bgcolor
from tkinter import *

window = tink.Tk()
window.geometry("500x500")
window.configure(bg = 'green')

def Signin():
    label = tink.Label(text = "Username?",font = ("Elephant",10,"bold"),bg='red')
    label.pack(side="top")

    entry = tink.Entry(window,bg="orange")
    entry.pack()

    label2 = tink.Label(text = "Password?",font = ("Elephant",10,"bold"),bg='red')
    label2.pack()

    entry2 = tink.Entry(window,bg="red",show ="*")
    entry2.pack()

    def save():
        x = entry.get()
        y= entry2.get()
        finallabel = tink.Label(text = "Saved",font = ("Elephant",10,"bold"),bg='red')
        finallabel.pack()
        final = {
            "Username" : x,
            "Pdw":y}
        
        print(final)

        def Yes():
            label3 = tink.Label(text="Ok",font = ("Elephant",10,"bold"),bg='red')
            
            label4 = tink.Label(text = "Username?",font = ("Elephant",10,"bold"),bg='red')
            label4.pack(side="top")

            entry4 = tink.Entry(window,bg="orange")
            entry4.pack()

            label5 = tink.Label(text = "Password?",font = ("Elephant",10,"bold"),bg='red')
            label5.pack()

            entry2 = tink.Entry(window,bg="red",show ="*")
            entry2.pack()

            def save():
                x = entry.get()
                y= entry2.get()
                finallabel = tink.Label(text = "Saved",font = ("Elephant",10,"bold"),bg='red')
                finallabel.pack()
                final = {
                    "Username" : x,
                    "Pdw":y}

            savebutton = Button(text = "Save",command = save, bg='blue', height = 2, width = 10)
            savebutton.pack()
        okbutton= Button(text = "Yes",command = Yes, bg='red', height = 2, width = 10)
        okbutton.pack()

        def No():
            Nolabel = tink.Label(text = "Ok Bye.")
            Nolabel.pack()
            quit()

        exitbutton = Button(text = "No -> Exit",command = No, bg='blue', height = 2, width = 10)
        exitbutton.pack()
    
    xbutton = Button(text = "Save",command = save, bg='blue', height = 2, width = 10)
    xbutton.pack()

xbutton = Button(text = "Sign in",command = Signin, bg='blue', height = 2, width = 10)
xbutton.pack()

window.mainloop()

