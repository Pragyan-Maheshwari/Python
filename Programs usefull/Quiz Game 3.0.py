import requests
Score = 0
Question_num = 0
Questions = 50

Data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
Data=Data.json()

i = 0

for i in range(11):
    print(Data["results"][i]["question"])
    x = input("[True(T/1)/False(F/0)] :- ")
    if x == "T" or "t" or "1":
        x= "True"
    elif x == "F" or "f" or "0":
        x= "False"

    if x.title() == Data["results"][i]["correct_answer"]:
        Score +=1
        Question_num +=1
        print("Your Answer is Correct")
        print(f"Score:- {Score}/{Question_num}")
    else:
        Question_num +=1
        print("Your answer is wrong... Try Again... Good Luck...")
        print(f"Score:- {Score}/{Question_num}")
    i+=1