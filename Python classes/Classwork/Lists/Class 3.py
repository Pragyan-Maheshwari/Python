Items = ["Coca cola 50$", "Pepsi 50$", "Pringles 100$"]
Cocacolacost = 50 ; Pepsicost = 50 ; Pringlescost = 100
print(Items)

Cola = int(input("How many cola u want?"))
Pepsi = int(input("How many Pepsi u want?"))
Pringles = int(input("How many Pringles u want?"))
print(f"your bill is {Cola*Cocacolacost + Pepsicost*Pepsi + Pringlescost*Pringles}")
print("Bye thanks enjoy.")