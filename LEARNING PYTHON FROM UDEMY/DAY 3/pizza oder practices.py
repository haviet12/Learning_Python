# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_bill=0
#choosen pizza size
if size=="S":
    total_bill+=15
elif size=="M":
    total_bill+=20
else:
    total_bill+=25

#choosen pepperoni for pizza size
if add_pepperoni=="Y":
    if size=="S":
        total_bill+=2
    else:
        total_bill+=3

#choosen cheese
if extra_cheese=="Y" :
    total_bill+=1

print(f"Your final bill is:${total_bill}.") 
