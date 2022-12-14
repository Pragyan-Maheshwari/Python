def add(x,y):
    return x + y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divide(x,y):
    return x/y

a = input("what is the first no. ")
b = input("what is the second no. ")
c = input("operator(+,-,/,*) ")

if c == "+":
    print(add(a,b))
elif c == "-":
    print(sub(a,b))
elif c == "*":
    print(multi(a,b))
elif c == "/":
    print(divide(a,b))