import random

print("Welcome to our restraunt!!")
print("How many people are with you?")
PeopleNo = input()

#if PeopleNo == int(PeopleNo):
PeopleNo = int(PeopleNo)
#else:
#    print("Please give a number and run the program again. Good Bye :)")
#    quit()

list = []

for i in range(PeopleNo):
    a = 1
    if PeopleNo > a:
        print("Welcome")
        n1 = input("What's your name?")
        list.append(n1)
        a=a+1

print("""At our place there is a rule.
We chose 1 person and He/She has to pay all the bill!!
Enjoy

So your bill is 50$
""")
pn = random.randint(0,len(list))
print(f"The number of the person is {pn+1}")
person = list[pn]
print(person)