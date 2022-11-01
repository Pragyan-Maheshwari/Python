import random

print("Welcome to the Pokemon Hangman")
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

stages = [
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

words = ["charmander","bulbasaur","squrdel"]

chosen = random.choice(words)
cl = list(chosen)

l = len(chosen)
dashes = "-"*l
dashes = list(dashes)

chances = 6 ; p=0 ; x=0 ; stage=stages[0] ; guessed = []

print(stages[x])
while p != chances:
    print(dashes)
    guess = input("What is your first guess? ")
    guessed.append = guess
    if guess not in guessed:
      guessed.append = guess
      if guess in chosen:
        for i in range(l):
          if chosen[i] == guess:
            if guess in dashes:
              print("Your have already used this letter")
            else:
              dashes[i] = guess
      else:
        x+=1
        stage=stages[x]
        print(stage)
        p +=1
    
    if dashes == cl:
      print("You won")
      print(f"The word was {chosen}")
      quit()
    
    if stage == stages[5]:
      print("You lost")
      print(f"The word was {chosen}")
