#Exam

#Q1
def oe(x):
    if x%2 == 0:
        return "This number is even"
    else:
        return "This number is odd"

num = int(input("Print you number"))
print(oe(num))