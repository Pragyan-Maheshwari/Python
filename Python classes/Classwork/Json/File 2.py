from curses import window
from tkinter import *
from email.mime import image
import tkinter as tink
from tkinter.ttk import Label
from PIL import ImageTk,Image
import json

win = tink.Tk()
win.title("Password Mannager")
win.geometry("600x600")

user_var=""
password_var=""

name  = Label(win,text ="password mannager")
name.pack()
name_lable = Label(win, text="Username")
name_lable.pack()
name_entry = Entry(win,textvariable="")
name_entry.pack()

password_lable = Label(win, text="password")
password_lable.pack()
password_entry = Entry(win,textvariable="")
password_entry.pack()

def submit():
    name=name_entry.get()
    password=password_entry.get()
    with open("data.json") as file:
        data = json.load(file)
    dict = {"username":name,'password':password}
    

