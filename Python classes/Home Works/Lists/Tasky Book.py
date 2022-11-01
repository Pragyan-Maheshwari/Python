print("Welcome to the Tasky Book")
print("Maxium amounts of tasks :- 5")
l = []
task1 = input("Please enter the first task ")
l.append(task1)

task2 = input("Please enter the task2 ")
l.append(task2)

task3 = input("Please enter the task3 ")
l.append(task3)

task4 = input("Please enter the task4 ")
l.append(task4)

add = input("Do you want to add any other task. Yes or No? ")
if add == "Yes".capitalize():
    add = input("What is the task? ")
    l.append(add)

change = input("Do you want to change any task? ")
if change.lower() == "yes":
    n = int(input("Please enter the number or the task"))
    length = len(l)
    if n > length:
        print(f"errorrrrrrr! {n} index not in rangeeee.")
    elif n <= length:
        task = input("What is the task? ")
        l.pop(n)
        l.insert(n,task)


i = ""
if i in l:
    l+=i
print(l)
print("So here are your tasks now get on doing them")
