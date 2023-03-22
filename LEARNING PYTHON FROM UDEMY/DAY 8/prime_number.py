def check_prime_number(number):
    #flag=0: is not prime number
    #flag=1: is prime number
    flag = 1
    if number<=2:
        flag = 0
        print(f'{a} is not prime number')
        return flag 

    else:
        for i in range(2,number):
            if number%i==0:
                print(f'{number} is not prime number')
                flag=0
                break
        return flag  

a = int(input('enter a number to check prime number: '))
n=check_prime_number(number=a) 
if n==1: 
    print(f'{a} is prime number')
