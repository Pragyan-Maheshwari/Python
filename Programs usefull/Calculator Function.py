def calsi(start,end,operation):
    if operation == "+":
        print(start+end)
    elif operation == "-":
        print(start-end)
    elif operation == "/":
        print(start/end)
    elif operation == "*":
        print(start*end)
    else:
        print("I dint get it.")

num1 = int(input("Please tell the 1st number"))
num2 = int(input("Please tell the 2st number"))
oper = input("Please tell the operator")
print(calsi(num1,num2,oper))
