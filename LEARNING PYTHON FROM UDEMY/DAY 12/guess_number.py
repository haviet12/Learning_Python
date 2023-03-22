from art_guess_number import logo
from random import choice
from click import clear


def play_game():
    #into game
    print(logo)
    print("""Welcome to Number Guessing Game!\n
    I'm thinking of a number between 1 to 100""")
    difficulty = input("Choose a difficuty. Type 'esay' or 'hard': ")

    # create a list from 0 to 100
    list_number=[]
    for number in range (1,101):
        list_number.append(number)


    # random a number fromm this list
    num=choice(list_number)

    # create a constant that it can change in 2 difficulty sitiuation 'hard' or 'esay'
    attemps=0
    if difficulty=='esay':
        attemps = 10
    if difficulty=='hard':
        attemps=5


    # create a function to compare number_guess with number randomed from list
    def compare(guess, num):
        if guess>100:
            print("Out of range")
        elif guess>num:
            print("Too hight.\nGuess again.")
        elif guess<num:
            print("Too low\nGuess again.")
        else:
            print(f"You got it!\nThe answer is {guess}")
            
    game_over=False
    while not game_over:
        if attemps<0:
            print("You Lose")
            game_over=True
        else:
            print(f"You have {attemps} attemps remaning to guess the number")

            # guess a number between 1 and 100
            guess=int(input("Guess a number: "))
            compare(guess, num)
            if guess == num:
                game_over=True
            attemps-=1

play_game()
next_game=input("Do you want to play new game?\nType 'y' to play new game or 'n' to end this game: ")
if next_game=='y':
    clear()
    play_game()
if next_game=='n':
    print("See you again".center(20,'*'))

