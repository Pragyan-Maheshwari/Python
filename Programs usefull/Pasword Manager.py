import random
Pdw = {
        "Gmail" : "Granny",
        "Snapchat" : "Nanny's Bolt",
        "Yahhoo" : "Boldunt",
        "Pokemon TCGN" : "Unbeatable Arceus",
        "Roblox" : "bruh",
        "RickRoll" : "Never Goona Give You Up :- https://www.youtube.com/watch?v=dQw4w9WgXcQ" }

r= True
while r:
    def add(Key,Value):
        Pdw.update({Key:Value})

    def remove(Key):
        Pdw.pop(Key)

    print(Pdw)
    print("")   
    
    inp = input("Would you like to view your Paswords or create a new Pasword or Delete a Pasword? Chose 'Add', 'Delete' or 'Change'?? ")
    print("")
    
    if inp.capitalize() == "Add":
        appn = input("App Name:- ")
        x = input("Would you like to genrate or enter? 'Genrate' or 'Enter'? ")
        if x.capitalize() == "Genrate":
            
            a = input("Enter something that can be use to make the password:- ")
            b = input("Enter something that can be use to make the password:- ")
            c = input("Enter something that can be use to make the password:- ")
            
            creation = [a,b,c]
            Pas = ""
            
            random.shuffle(creation)
            for x in creation:
                Pas += x
            
            print(f"Your pasword is :- {Pas}")
            add(appn,Pas)
        else:
            add(appn,input("app pasword - "))
    
    elif inp.title() == "Delete":
            remove(input("removing app name - "))

    elif inp.capitalize() == "Change":
        appn = input("App Name:- ")
        x = input("Would you like to genrate or enter? 'Genrate' or 'Enter'? ")
        if x.capitalize() == "Genrate":
            
            a = input("Enter something that can be use to make the password:- ")
            b = input("Enter something that can be use to make the password:- ")
            c = input("Enter something that can be use to make the password:- ")
            
            creation = [a,b,c]
            Pas = ""
            
            random.shuffle(creation)
            for x in creation:
                Pas += x
            
            print(f"Your pasword is :- {Pas}")
            add(appn,Pas)
        else:
            add(appn,input("app pasword - "))
    
    print("")
    print(Pdw)

    print("")
    h = input("Would you like to change any thing else? 'Yes' or 'No'? ")
    if h.title() == "Yes":
        r = True
    else:
        print("Bye!")
        r = False
