def h(x,n):
    if x in n:
        return "This item is in it"
    else:
        return "this item is not in it"

p= ["x","h","9",3,4,True,0.4]
print(h("x",p))