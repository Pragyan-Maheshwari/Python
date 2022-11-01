import tkinter as Tikki

window = Tikki.Tk()
window.title("My first GUI.")
window.minsize(width=500, height=500)
window.geometry("500x500")


my_lable = Tikki.Label(text="I am a Disco Master",font=("Arial",25,"bold"))
my_lable.pack(side="left")

window.mainloop()