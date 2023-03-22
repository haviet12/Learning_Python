import art_blind_auction

import click

print('wellcome to secret auction programe')

def highest_price(dict_bid):
    winner=''
    max = 0
    for key in dict_bid:
        a=dict_bid[key]
       
        if a>max :
            max=a
            winner=key
    print(f"the winner of auction is {winner} with ${max}")
       
dict={}

finish = False
while not finish:
    name = input("What's Your Name: ")
    bid = int(input("What's Your Bid: "))

    dict[name]=bid
    direction = input("Are there any bidders in this auction: ")

    if direction == 'Yes':
        click.clear()
    if direction == 'No':
        click.clear()
        highest_price(dict_bid=dict)
        finish = True