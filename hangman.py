import numpy as np
import os
list_of_words=["camel","mortalcombat","madmax"]
gess_word=[]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

i=np.random.randint(0,len(list_of_words))
choosen_word=list_of_words[i]
life=0
gess_word.clear()
for i in choosen_word:
    gess_word.append('-')
 
while 1 :
    os.system('cls')
    for i in gess_word:
        print(i,end='')
    print()
    print(HANGMANPICS[life])
    gess_letter=input("ges a letter:")
    
    if gess_letter in choosen_word:
        print("right")
        for i in range (len(choosen_word)):
            if choosen_word[i]==gess_letter:
                gess_word[i]=gess_letter  
        if "-" not in gess_word :
            os.system('cls')
            print(choosen_word)
            print(HANGMANPICS[life])
            print("win")
            break

    else:
        print("wrong")
        life+=1
        if life==6:
            os.system('cls')
            print(HANGMANPICS[life])
            print(f"word was: {choosen_word}")
            print("loose")
            break