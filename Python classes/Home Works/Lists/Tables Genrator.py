# Welcome
print("Welcome to the table gentrator...")
nme = input("What's your name?")
print(f"Welcome {nme}...")

# Taking Input
StartNum = int(input("Please enter the starting number you want to print tables from... "))
EndNum = int(input("Please enter the ending number you want to print tables to... "))
PrintingNum = 1
Runtime = True

# Printing Tables
while Runtime == True:
    print(f"Table of {StartNum}")
    for i in range(1,11):
        print(f"{StartNum} * {PrintingNum} = {PrintingNum * StartNum}")
        PrintingNum = PrintingNum + 1
    if StartNum == EndNum:
        Runtime = False
    StartNum = StartNum + 1
    PrintingNum = 1