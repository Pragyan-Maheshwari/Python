story = """This is a story of man named RAHUL, who lived in a village.He had 5 cows ,3 goats,1 dog 
and 6 chicken in his farm land. His wife was a farmer who had a land of 14 acers which grew rice, groundnut,
sugarcane on basis area and plantation. """
## use a abstact data structure and store the different domestic animals and also the types of plants.
## scrap the data using string sclicing

animals = []
animals.append(story[68:72])
animals.append(story[76:81])
animals.append(story[84:87])
animals.append(story[95:102])
#print(animals)

plants = []
plants.append(story[181:185])
plants.append(story[187:196])
plants.append(story[198:207])
#print(plants)

#"""Here there is a number convert to a string find the exponent  """
#"""The exponent of the number is given as 2**2 == 4"""
q=2**2
#print(q)

""" Create a winner checker game based on the scores in the following sets of table tennis
1) Each set  contains of 40 point for 30 min 
2) By the end of 30 min scores will be given in the form of user input 
3) And check who is the winner by normal if statements and format strings to declare the winner with the score."""

print("start")
print("End")
player1 = int(input("what is the first player's score"))
player2 = int(input("what is the second player's score"))

if player1 == player2:
    print("it's a tie")
elif player1 > player2:
    print("Player 1 wins")
elif player1 < player2:
    print("Player 2 wins")

n1 = int(input("Give the first number"))
n2 = int(input("Give the second number"))
n3 = int(input("Give the third number"))
a = ""
if n1 > n2:
    a = n1
    if n1 <n3:
        a = n3
elif n1<n2:
    a = n2
    if n2 <n3:
        a = n3
print(a)

#' ----------------MY REPORT--------------- '
# SUB                                MARKS
# MATH                                 96
# SCI                                  95

q = "MY REPORT"
d = "SUB"
f = "MATH"
h = "SCI"

print(q.center(30,"-"))
d = d.ljust(30," ") + "MARKS"
f=f.ljust(30," ") + "96"
h=h.ljust(30," ") + "95"
print(f"{d}\n{f}\n{h}")

#"""Given a list find the sum of the elements in the list """
data = ["123","456","234","456","111"]
q = int(data[0])
w = int(data[1])
e = int(data[2])
r = int(data[3])
t = int(data[4])
print(q+w+e+r+t)

#"""Write few sentences on your favorite topic in python (Descriptive)"""
print("""I dont have any favorite topic in python. I like to code in python. """)

#"""Write few words on dynamic typing"""
print("""???????????""")