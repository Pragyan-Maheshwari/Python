print("""Welcome to Fuse Name Creator.
Here we will create a new name by taking the 1st two letters of 5 names""")
n1 = input("Name 1:- ")
n2 = input("Name 2:- ")
n3 = input("Name 3:- ")
n4 = input("Name 4:- ")
n5 = input("Name 5:- ")

Creation = n1[0:2]+n2[0:2]+n3[0:2]+n4[0:2]+n5[0:2]
Creation = Creation.capitalize()
print(f"So The Fused Name Is :- {Creation}")