import tkinter as Tink

window = Tink.Tk()
window.title("Pragyan :- 'Hi Dumb Mritunjay.'")
window.minsize(width=600, height=600)
window.geometry("600x600")


my_lable = Tink.Label(text="I Am The Almighty God",font=("Arial",30,"bold"))
my_lable.pack(side="top")

window.mainloop()