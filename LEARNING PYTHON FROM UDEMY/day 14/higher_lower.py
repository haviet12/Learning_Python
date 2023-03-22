from click import clear
from art import logo, vs
from data_game import data
from random import randint

def play_game():
    # tạo 1 hàm để in ra thông tin đối tượng A
    def object_A(index_A):
        compare_A = data[index_A]
        info_A= compare_A['name']+','+compare_A['description']+','+compare_A['country']
        print("Compare_A: ",info_A)
        

    # tạo 1 hàm để in ra thông tin đối tượng B
    def object_B(index_B):
        compare_B = data[index_B]
        info_B= compare_B['name']+','+compare_B['description']+','+compare_B['country']
        print("Compare_B: ",info_B)
        

    # print(logo)
    score=0
    game_over=False
    while not game_over:
        # random 1 số bất kì trong khoảng từ 1 đến 48 để lấy 2 đối tượng bất kì từ data
        num_A= randint(1,48)
        num_B= randint(1,48)
        if num_A==num_B:
            num_B= randint(1,48)

        A=data[num_A]['follower_count']
        B=data[num_B]['follower_count']

        
        object_A(index_A=num_A)  
        print(vs)
        object_B(index_B=num_B)  
        # chọn 1 đôi tượng bất kì mà bạn nghĩ là có lượt follow cao hơn
        choosen = input("choose a subject if you think it have more follower.\nType 'A' or 'B': ")
        if choosen =='A':
            if A>B:
                clear()
                score+=1
                print(logo)
                print(f"You're Right! Your current score is {score}")
            else:
                clear()
                print(logo)
                print(f"You Lose. Your current score is {score}") 
                game_over=True
        elif choosen =="B":
            if A<B:
                clear()
                score+=1
                print(logo)
                print(f"You're Right! Your current score is {score}")
            else:
                clear()
                print(logo)
                print(f"You Lose. Your current score is {score}") 
                game_over=True
a=5
b=1
print(logo)
play_game()
while a>b:
    
    next_game=input("Do you want to play new game?\nType 'y' to play new game or 'n' to end this game: ")
    if next_game=='y':
        clear()
        print(logo)
        play_game()
    if next_game=='n':
        print("See you again".center(20,'*'))
        b=6




