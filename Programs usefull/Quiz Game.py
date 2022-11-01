print("Welcome to the Quiz Game...")

quiz = {
    "Sky is blue." : "True",
    "Sun is hot." : "True",
    "Water is universal solvent." : "True",
    "Water is needed by our body." : "True",
    "Polution is bad for our environment" : "True"}

Score = 0

for i in quiz:
    print(i)
    Ans = input("What is the answer to the above statement 'True' or 'False' ???").title()

    if Ans == quiz[i]:
        print("Your correct!!!")
        Score = Score + 1
        print(f"Your score is {Score}")
    else:
        print("Better luck next time.")
print("Game over!")
print(f"Your final score is {Score}")