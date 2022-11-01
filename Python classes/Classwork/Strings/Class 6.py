str = "Today\"s my birthday"
#print(str)
str2 = "I am a super active person"
#print(str2.startswith("I"))
str3 = ["Hi","aaj","chai","peethe","hai"]
str4 = str3[0]+str3[1]+str3[2]+str3[3]+str3[4]
#print(str4)

a = ""
for i in str3:
    a = a+i
    a = a+" "
#print(a)
b = "Hi ho kese hai coffee"
print("#".join(str3))
#print(b.split(" "))
c = "Good Morning"
print(c.rjust(50,"-"))
print(c.ljust(50,"-"))
print(c.center(50,"&"))