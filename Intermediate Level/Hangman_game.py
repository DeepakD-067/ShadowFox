Stages = ['''

    +- - - - +
    |   |    |
    |   O    |
    |  /|\   |
    |  / \   |
    |        |
    +========+
    ''','''
    +- - - - +
    |   |    |
    |   O    |
    |  /|\   |
    |  /     |
    |        |
    +========+
    ''','''
    +- - - - +
    |   |    |
    |   O    |
    |  /|\   |
    |        |
    |        |
    +========+
    ''','''
    +- - - - +
    |   |    |
    |   O    |
    |  /|    |
    |        |
    |        |
    +========+
    ''','''
    +- - - - +
    |   |    |
    |   O    |
    |   |    |
    |        |
    |        |
    +========+
    ''','''
    +- - - - +
    |   |    |
    |   O    |
    |        |
    |        |
    |        |
    +========+
    ''','''
    +- - - - +
    |   |    |
    |        |
    |        |
    |        |
    |        |
    +========+
    ''']


import random as r
print("Lets play Hangman !!!")

lives=6

list_words=["apple","banana","mango","orange","grapes"]
word=r.choice(list_words)
print("You have only 6 lives so try to gues the word within 6 attemps!!")
display=[]
for i in range(len(word)):
    display+= '_'
print(display)

game_over=False
while not game_over:
    guess=input("Guess a letter: ")
    for position in range(len(word)):
        if guess == word[position]:    
            display[position]=guess

    print(display)
    if guess not in word:
        print(f"You guessed {guess} that is not present in the word. So you lose the life!!")
        lives-=1
        if lives==0:
            game_over=True
    if '_' not in display:
        game_over=True
        print("You Win!!!")
    print(Stages[lives])
        
      
    


