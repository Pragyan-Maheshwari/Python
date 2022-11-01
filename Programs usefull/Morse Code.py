print("Welcome to the Morse Coder.")
Morse_Code = {
    'a':'.-', 
    'b':'-...',
    'c':'-.-.', 
    'd':'-..', 
    'e':'.',
    'f':'..-.', 
    'g':'--.', 
    'h':'....',
    'i':'..', 
    'j':'.---', 
    'k':'-.-',
    'l':'.-..', 
    'm':'--', 
    'n':'-.',
    'o':'---', 
    'p':'.--.', 
    'q':'--.-',
    'r':'.-.', 
    's':'...', 
    't':'-',
    'u':'..-', 
    'v':'...-', 
    'w':'.--',
    'x':'-..-', 
    'y':'-.--', 
    'z':'--..',
    
    '1':'.----', 
    '2':'..---', 
    '3':'...--',
    '4':'....-', 
    '5':'.....', 
    '6':'-....',
    '7':'--...', 
    '8':'---..', 
    '9':'----.',
    '0':'-----', 
    
    ', ':'--..--', 
    '.':'.-.-.-',
    '?':'..--..', 
    '/':'-..-.', 
    '-':'-....-',
    '(':'-.--.',
    ')':'-.--.-',
    ' ':' '
    }

#k = input("Would you like to decode Morse Code or translate something to Morse Code? Type 'Code' or 'Decode'. ")
#if k.lower == "code":
h = input("What do you want to translate to Morse Code? ").lower()
x = list(h)
a=0
Tranced = ""

for i in range(len(x)):
    n = x[a]
    Tranced = Tranced + Morse_Code[n]
    a = a+1
print(h)
print(Tranced)