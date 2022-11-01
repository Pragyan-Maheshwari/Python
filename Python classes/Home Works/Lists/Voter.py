#Side Code:
import random


# Main Program:
VoteingLine = [ "Adars" , "Amit" , "Arun", "Bhuvan","Bindar","Chand","Deepak","Diya" ,"Harpreeth","Himanshu" , "Jaggu","Lakshmi","Mrityunjaya","Mayank", "Mahesh" ,"Namita","Naveen" ," Om","Pragyan","Ramesh","Suresh" ,"Zoya"]
print("""Congratulations !! ..You have tured 18 year old .. And now you can vote for the nation .. And today voting is going on in our city.
So please chose a wise leader to vote to...
...

So lets go to the pooling booth...
...

There it is...

Good Morning!""")

print(VoteingLine)

Nme = input("What is your name?")
if Nme in VoteingLine:
    n = VoteingLine.index(Nme)
else:
    print("Error..Your name is not in the society list please retry.")
    quit()

q=n
w=q
for i in range(q):
    VoteingLine.pop(0)
    print(VoteingLine)
    print(f"""Your number is {w}.""")
    w = w-1

print("Finaly it is your turn to vote.")