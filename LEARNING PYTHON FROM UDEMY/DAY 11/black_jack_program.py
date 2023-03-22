import random
from random import choice
import black_jack_art
from click import clear
cards_value =[11,2,3,4,5,6,7,8,9,10,10,10,10]

# tạo hàm deal_card() để random ra 2 thẻ bài cho player và computer 
def deal_card():
    for card in range(0,2):
        player_cards.append(choice(cards_value))
        computer_cards.append(choice(cards_value))
    print(f'Your Cards: {player_cards}, current score = {player_cards[0]+player_cards[1]}')
    print(f'The first card of computer: {computer_cards[0]}')

# tạo hàm get_player_cards() với tham số là your_timer để lấy thêm 1 lá bài cho player 
def get_player_cards( your_timer):
    value_player_card=0
    player_cards.append(choice(cards_value))
    if sum(player_cards)>21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
    for i in range(0, your_timer):
        value_player_card+=player_cards[i]
    print(f'Your Cards: {player_cards}')
    return value_player_card

# tạo hàm get_computer_cards() với tham số là computer_timer để lấy thêm 1 lá bài cho computer
def get_computer_cards(computer_timer):
    value_computer_card=0
    computer_cards.append(choice(cards_value))
    if sum(computer_cards)>21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
    for i in range(0, computer_timer):
        value_computer_card+=computer_cards[i]
        if value_computer_card >18:
            return value_computer_card
    return value_computer_card

# tạo hàm compare_cards() để so sánh giá trị bài cảu player và computer

def compare_cards(value_computer_card, value_player_card):
    # TH1: cả 2 đều có điểm nhỏ hơn 21, bài ai cao hơn thì người đó thắng
    if value_computer_card<=21 and value_player_card<=21:
        #Computer win
        if value_computer_card>value_player_card :
            print("Game Over!\nYou lose")
        # Player Win
        elif value_computer_card<value_player_card :
            print("Game Over!\nYou Win")

    #TH2: 1 trong hai có điểm lớn hơn 21
    if value_computer_card >21 or value_player_card>21:
        # Player Win
        if value_computer_card>21 and value_player_card<21:
            print("Game Over!\nYou Win")
        # Computer Win
        elif value_computer_card<21 and value_player_card>21:
            print("Game Over!\nYou lose")
    
    # TH3: cả 2 đều có số điểm bằng nhau hoặc cả hai đều có số điểm lớn hơn 21
    elif value_computer_card == value_player_card :
        print('Game Over.\nDRAW')
    elif value_player_card>21 and value_computer_card>21:
        print('Game Over.\nDRAW')
    
    


# tạo list các lá bài cho player và computer  
player_cards =[]
computer_cards=[]  
deal_card()


player_score=player_cards[0]+player_cards[1]
computer_score=computer_cards[0]+computer_cards[1]


# tạo biến đếm với số bài hiện có để bốc bài cho player và computer
your_timer=2
computer_timer=2


game_over = False
while not game_over:
    # 2 trường hợp đặc biệt là player được BLACKJACK hoặc computer được BLACKJACK
    if player_score ==21 and len(player_cards)==2:
        print('BLACKJCAK\nGame Over.\nYou win')
        game_over= True
    if computer_score ==21 and len(computer_cards)==2:
        print(f'computer_cards: {computer_cards} and total value is: {computer_score}')
        print('BLACKJACK\nGame Over.\nComputer win')
        game_over= True
    # trường hợp không có BLACKJACK 
    option = input("Type 'y' to get another card or type 'n' to pass: ")
    if option == "y":
        your_timer+=1
        player_score =get_player_cards(your_timer)

    elif option=='n' :
        while computer_score<17:
            computer_timer+=1
            computer_score=get_computer_cards(computer_timer)
        print(f'computer_cards: {computer_cards} with current score is: {computer_score}')
        print(f"Your cards are:{player_cards} with current score is:{player_score}")
        compare_cards(value_computer_card=computer_score, value_player_card=player_score)
        game_over= True
        
           


