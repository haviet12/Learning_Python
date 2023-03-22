sum_even_numbers = 0
for i in range (2, 101):
    if i%2==0:
        sum_even_numbers +=i
    else:
        continue
print(f"sum of even numbers form 2 to 100 is: {sum_even_numbers}")

