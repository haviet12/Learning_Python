# DECLEARE LIBRARY
from random import choice 
import art_hangman 
from art_hangman import lives

#T01: random a word from words_list and trans this word into list
words_list=['love','career','money','family']
word = choice(words_list)
list_letter=list(word)
#print(word)

#T02: calcu len of word and make the blanks equal this
bl='_'
list_blanks=bl.split()*len(word)

#T03: compare the letter you guessed with letter in word

print(f'word has {len(word)} letter and start with letter {list_letter[0]} ')

a= 6
while a>0:
    blanks=""
# find guess in word and replace blank by them    
    guess = input("guess a letter which you think this letter is in the word: ").lower()
    if guess in word:
        
        for i in range (0,len(list_letter)):
            if guess==list_letter[i]:
                list_blanks[i]=guess
            else:
                continue
    else:
        a = a-1
# export resoult after compare and replace     
    print(lives[6-a])
    for j in range(len(list_blanks)):
        blanks +=list_blanks[j]
    print(blanks)
    if word == blanks:
        print('Game Over\nYou Win')
        break
    else:
        continue
    
else:
    print('Game Over\nYou Lose')
