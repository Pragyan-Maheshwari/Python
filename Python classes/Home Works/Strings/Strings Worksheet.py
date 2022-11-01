Umb = "Umbrella"
if "e" in Umb:
    print("'e' is there in Umbrella")
else:
    print("'e' isn't there in Umbrella")

Juice = "This is a orange juice"
if "orange" in Juice:
    print("'orange' is there in the sentence 'This is a orange juice'")
else:
    print("'orange' isn't there in the sentence 'This is a orange juice'")

Name = "Jhon Smith"
n_line='0123456789'
print(Name[1])
# This will print the 2nd letter that is 'h'

print(Name[-2])
# This will print the 2nd last letter that is 't'

print(Name[1:-1])
# This will print 2nd letter to 2nd last letter.
# It is because 0 represents the first letter. 

print(len(Name))
# This function will print the length of 'Name' varible

mp = f"{2+2}+{10%3}"
print(mp)
# This will print 4+1 because 2+2 = 4 and 10%3 = 1 so 4+1 = 5

print(Name.title())
# Name.title() will return name titled means it will make every first letter of a word capital
print()