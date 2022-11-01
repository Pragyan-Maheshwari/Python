#Q1. Create a student administration system

s1 = {"Student" : "pragyan",
"Parent":"Vikalp",
"role no":927343,
"class":7,
"section":"D"}
print(s1)

d = input("do you want to add any student?").lower()
if d == "yes":
   s1["Student"] = input("student name ") 
   s1["Parent"] = input("parent name ") 
   s1["role no"] = input("role no ") 
   s1["class"] = input("class ") 
   s1["section"] = input("section ") 


x = input("do you want to change any thing? Yes or No?").title()
if x == "Yes":
    n = input("what? ").title()
    if n == "Student":
        x = input("Student name? ")
        s1["Student"] = x
    elif n == "Parent":
        x = input("Parent name? ")
        s1["Parent"] = x
    elif n == "role no":
        x = input("role no? ")
        s1["role no"] = x
    elif n == "class":
        x = input("class? ")
        s1["class"] = x
    elif n == "section":
        x = input("section? ")
        s1["section"] = x
