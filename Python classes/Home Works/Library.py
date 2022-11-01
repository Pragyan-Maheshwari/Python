def add(n,x):
    Books.update({n:x})
Books = {
    "The Secrets of Life" : 3,
    "The Secrets of Coding" : 5,
    "The life of jungle": 2,
    "The power of positivity":6,
    "Power of Now":5,
    "7 Habits of Highly effective people":8}

People = {
    "Admin" : "Pragyan",
    "user" : ["Nimisha","Vikalp"]
}

n = input("What's your name?").title()

if n in People["user"]:
    print(Books)
    c = input("do you want to borrow any book or Return ? ").title()
    if c == "Borrow":
        borrowing = input("which book? please dont do any spelling mistakes ")
        if borrowing in Books:
            print(f"Here you go. Your book {borrowing}. And you have to return the book in 10 days or else you will have to pay fine.")
            Books[borrowing] -=1
            print(Books)
            print("10 days later...")
            print("")
            print("")
            print("You came back...")
            print("")
            print("You returned the book...")
            print("")
            print("You went...")
            print("")
            Books[borrowing] +=1
        else:
            print("Check for spelling mistakes etc. ")
    
    elif c == "Return":
        x = input("What book you want to return ")
        Books[x]+=1

elif n == People["Admin"]:
    print(Books)
    work = input("Do you want to 'Add' or 'Delete' or 'Update' ")
    if work == "Add":
        NewBook = input("New Book : ")
        x = input("what is the quantity? ")
        add(NewBook,x)
    elif work == "Delete":
        Delete = input("Which book you want to delete? ")
        Books.pop(Delete)
    elif work == "Update":
        h = input("What book quantity do you want to update? ")
        n = input("What quantity? ")
        Books[h] = n
print(Books)
print("Bye thx ")