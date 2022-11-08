from tkinter import *
  
tink = Tk()
tink.geometry("150x200")
   
scroll_bar = Scrollbar(tink)
  
scroll_bar.pack( side = RIGHT,fill = Y )
   
list = Listbox(tink, yscrollcommand = scroll_bar.set )
   
for line in range(1, 70):
    list.insert(END,str(line))
  
list.pack( side = LEFT, fill = BOTH )
  
scroll_bar.config( command = list.yview )
   
tink.mainloop()