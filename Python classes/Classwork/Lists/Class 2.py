#q = int(input("Enter the number u Check is odd or even"))

#o = q%2
#if o==1:
    #print('it is odd num')
#elif o == 0:
    #("the number is even")

no1 = int(input())
n2 = int(input())
n3 = int(input())

if no1 >n2:
    if no1 >n3:
        print(f"{no1} is the greatest number")
    else:
        print(f"{n3} is the greatest number")
elif no1 >n3:
    if no1 >n2:
        print(f"{no1} is the greatest number")
    else:
        print(f"{n2} is the greatest number")

elif n2 >n3:
    if n2 >no1:
        print(f"{n2} is the greatest number")
    else:
        print(f"{no1} is the greatest number")
elif n2 >no1:
    if n2 >n3:
        print(f"{n2} is the greatest number")
    else:
        print(f"{n3} is the greatest number")

elif n3 >no1:
    if n3 >n2:
        print(f"{n3} is the greatest number")
    else:
        print(f"{n2} is the greatest number")
elif n3 >n2:
    if n3 >no1:
        print(f"{n3} is the greatest number")
    else:
        print(f"{no1} is the greatest number")
else:
    print("all are equal")