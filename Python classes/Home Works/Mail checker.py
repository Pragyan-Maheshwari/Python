email = input("What is your email id ")

Real = ["@gmail.com","yahoo.com","proton.me","rediff.com","hotmaid.com"]
r = False

if "@" in email:
    split = email.split("@")
    print(split)
else:
    print("Your email is Fake...")
