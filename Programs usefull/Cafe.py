N = input("""Welcome To Our Caffee Sir/Mam.
What's Your Name? """)
print(f"Welcome {N}")
print("Here's The Menu:-")
#Menu
Mnu = """Coffee:-
Black Coffee                                10$
Americano Coffee                            20$
Cold Brew Coffee                            45$
Cappuccino Coffee                           15$
Kopi luwak                                  400$

Sandwitch:-
Potato Sandwitch                            40$
Mayo Sandwitch                              60$
Cheese Sandwitch                            90$
Kwality Wall'S Ice Cream Sandwitch          50$

Ice Cream:-
Kwality Wall'S Choco Bar                    20$
Kwality Wall'S Vanila Cup                   10$
Kwality Wall'S Tuti-Fruity Cup              12$
Kwality Wall'S Ice Cream Sandwitch          50$"""
print(Mnu.lower().upper().casefold().capitalize().swapcase().title())
L=input("What List Do you want to order from? ")
print("")

if L == "Coffee":
    Ofc=input("Black Coffee, Americano Coffee, Cold Brew Coffee, Cappuccino Coffee, Kopi luwak. What do you want to order? ")
    if Ofc == "Black Coffee":
        print("Thank you for buying.\n Your bill is 10$")
    if Ofc == "Americano Coffee":
        print("Thank you for buying.\n Your bill is 20$")
    if Ofc == "Cold Brew Coffee":
        print("Thank you for buying.\n Your bill is 45$")
    if Ofc == "Cappuccino Coffee":
        print("Thank you for buying.\n Your bill is 15$")
    if Ofc == "Kopi luwak":
        print("Thank you for buying.\n Your bill is 400$")

elif L=="Sandwitch":
    Ofs=input("Potato Sandwitch, Mayo Sandwitch, Cheese Sandwitch, Kwality Wall'S Ice Cream Sandwitch.\nWhat do you want to order? ")
    if Ofs == "Potato Sandwitch":
        b = "40"
        if b.isdigit() == True:
            print("Thank you for buying.\n Your bill is 40$")
    if Ofs == "Mayo Sandwitch":
        print("Thank you for buying.\n Your bill is 60$")
    if Ofs == "Cheese Sandwitch":
        print("Thank you for buying.\n Your bill is 90$")
    if Ofs == "Kwality Wall'S Ice Cream Sandwitch":
        print("Thank you for buying.\n Your bill is 50$")

elif L=="Ice Cream":
    Ofi=input("Kwality Wall'S Choco Bar, Kwality Wall'S Vanila Cup, Kwality Wall'S Tuti-Fruity Cup, Kwality Wall'S Ice Cream Sandwitch.\nWhat do you want to order? ")
    if Ofi == "Kwality Wall'S Choco Bar":
        bill = "20"
        if bill.isdecimal() == True:
            print(f"Thank you for buying.\n Your bill is {bill}$")
    if Ofi == "Kwality Wall'S Vanila Cup":
        bll = "10"
        if bll.isnumeric() ==True:
            print("Thank you for buying.\n Your bill is 10$")
    if Ofi == "Kwality Wall'S Tuti-Fruity Cup":
        print("Thank you for buying.\n Your bill is 12$")
    if Ofi == "Kwality Wall'S Ice Cream Sandwitch":
        print("Thank you for buying.\n Your bill is 50$")

else:
    print("""I dint understand that. Please Retry
    The List are:-
    Coffee
    Sandwitch
    Ice Cream""")

feedback = input("Hi Please Give Us Some Feedback\n")
fb = feedback.replace(" ","")

if fb.isalpha() == True:
    print("All the Feedback was in text do u want to give some rating?")
    Rating = input("Yes or No?")
    if Rating.lower() == "yes":
        input("Please give some rating in stars'*'")
        print("Thank you")
        if feedback.islower() == True:
            print("Please Visit Again!\nBye!")
        elif feedback.isupper() == True:
            print("Please Visit Again!\nBye!")
        elif feedback.istitle() == True:
            print("Please Visit Again!\nBye!")
    elif Rating.lower == "no":
        print("Ok, No Problem")

elif fb.isalnum == True:
    print((f"Your Feedback:- {feedback}\nThank You!").count(" "))
