from art_calculater import logo
from click import clear

def calculate(n1, n2, operation):
    if operation == '+':
        result = n1 + n2
    elif operation == '-':
        result = n1 - n2
    elif operation == '*':
        result = n1 * n2
    elif operation == '/':
        result = n1 / n2
    return int(result)

operation_list=['+','-','*','/']
def calc():
    print(logo)
    num1 = int(input("What's the first number? "))
    while True:
    
        for op in operation_list:
            print(op)
        function_cal = input("What's the operation you want? ")
        num2 = int(input("What's the second number? "))
        answer=calculate(n1=num1,n2= num2, operation=function_cal)
        print(answer)
        option=input(f"Type 'y' if you want to calculate with {answer} or Type 'n' if you want to calculate with a new number")
        if option == 'y':
            num1=answer
    
        elif option=='n':
            clear()
            calc()
calc()