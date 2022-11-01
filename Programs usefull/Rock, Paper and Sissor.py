import random
print("""Welcome To the Rock, Paper and Scissor!!
Commands -> Scissor, Paper and Rock
Scissor > Paper
Paper > Rock
Rock > Scissor
""")
List = ["scissor", "rock ", "paper"]
for i in range(10):
    comp = random.choice(List)
    player = input("> ").lower()
    comp = comp.title()
    print(comp)
    comp = comp.lower()
    if player not in List:
        print("I Dont Understand That")
    elif player == "help":
        print("""Commands -> Scissor, Paper and Rock
Scissor > Paper
Paper > Rock
Rock > Scissor""")
    elif comp == player:
        print("It's A Tie")
    elif comp == "scissor" and player == "paper":
        print("Computer Wins!!!")
    elif comp == "scissor" and player == "rock":
        print("You Win!!!")
    elif comp == "rock" and player == "paper":
        print("You Win!!!")
    elif comp == "rock" and player == "scissor":
        print("Computer Wins!!!")
    elif comp == "paper" and player == "scissor":
        print("You Win!!!")
    elif comp == "paper" and player == "rock":
        print("Computer Win!!!")
