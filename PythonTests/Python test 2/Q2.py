#Q2. Create a simple calculator - take 2 operants 1 operator

def divide(h,v):
    print(h/v)
def sub(h,v):
    print(h-v)
def multi(h,v):
    print(h*v)

n1 = int(input("what is the first number?"))
n2 = int(input("What is the 2nd number? "))
oper = input("what is the operator? ")

if oper == "*":
    multi(n1,n2)
elif oper == "/":
    divide(n1,n2)
elif oper == "-":
    sub(n1,n2)
elif oper == "+":
    print(n1+n2)