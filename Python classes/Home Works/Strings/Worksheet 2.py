# 1. Take a string, display only those characters which are present at an even index number.
s = "I am learning Python!!"
s = s[0:22:2]
print(s)
# Done!!!

# 2. Strip the given string of unnecessary whitespaces and 
# change the case of nouns into uppercase and leave the rest of the string as it is. 

str1 = " Hello, I'm John and I live in the United States. "
# So we will use strip first.
str1 = str1.strip(" ")
# done.
# now to make the nouns upper.
str1 = str1.replace("Jhon","JHON")
str1 = str1.replace("United States","UNITED STATES")
print(str1)
#done
# 3. Replace the question marks in the string with exclamation marks.
str2 = "Watch out??? There's a rock ahead?"
str2 = str2.replace("?","!")
print(str2)
#done.
# 4. Write a program to find the first and the last occurence of the letter 'o' and character ',' in "Hello, World"./
h = 'Hello, World'
print(h.rfind("o"))
print(h.find("o"))
print(h.rfind(","))
print(h.find(","))
# 5. Write the string after the first occurrence of ',' and the string after the last occurrence of ',' in the string "Hello, Good Morning, World".

x = "Hello, Good Morning, World"
print(x.find(","))
print(x.rfind(","))

# 6. What is the result of this expression: “*” * 10    # hint : print("*" * 10)
d = "*"
print(d*10)

# 7.Write a program to take a sentence from the user and print out the longest word in the sentence.
# for ex = "This is a story of Shivaji"
# o/p = Shivaji --- (7) is the length
user_input = input("Enter the sentence from which you want the longest word:- ")
u = user_input
user_input=user_input.split(" ")
max_length = 0

for word in user_input:
    Lengther = len(word)
    if Lengther > max_length:
        max_length = Lengther
        Name = word

print(max_length)
print(Name)
print(f"It is on {Name.find(u)} place in the sentence you gave")