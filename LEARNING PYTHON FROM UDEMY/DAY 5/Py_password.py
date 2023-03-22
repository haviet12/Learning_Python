# DECLEARE LIBRARY
import random as r
from random import choice
#PREPARE DATA FOR PASSWORD
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
        'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
        'R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','#','$','%','&','+','-','/',':','<','=','>','?','@','[',']','^','_','`','{','|','}','~']

#INITIALIZATION PASSWORD
print('Welcome to the generator password')
a = int(input('How many letter would you like in your password? \n'))
b = int(input('How many number would you like in your password? \n'))
c = int(input('How many symbols would you like in your password? \n'))

# EAZY LEVEL

#pass_letter = " "
#for i in range (0,a):
#    pass_letter += choice(letter)
#pass_number =" "
#for j in range (0,b):
#    pass_number += choice(number)
#pass_symbol = " "
#for k in range (0,c):
#    pass_symbol += choice(symbol)

#password = pass_letter+pass_number+pass_symbol
#print(f"password: {password}")

# hard level
password_list =[]
pass_letter =[]
pass_number =[]
pass_symbol =[]
for i in range (0,a):
    pass_letter.append(choice(letter)) 

for j in range (0,b):
    pass_number.append(choice(number)) 

for k in range (0,c):
    pass_symbol.append(choice(symbol))  

password_list = pass_letter+pass_number+pass_symbol
r.shuffle(password_list)
password=" "
for i in range (0,len(password_list)):
    password += password_list[i]
print(f"password: {password}")