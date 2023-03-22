import random 
'''import test_link_random
random_int = random.randint(1, 100)
print('your random int is: ',random_int)

'''
'''
TEST LINK MODULE IN PYTHON
a= test_link_random.pi*2
print(a)'''
'''
#RANDOM A FLOAT NUMBER FROM 0 TO 1 ( NOT INCLUDING 1)
random_float = random.random()
print('random_float is: ',random_float)

#RANDOM A FLOAT NUMBER FROM 0 TO AN ANY NUMBER ( NOT INCLUDING THAT NUMBER)
A= random_float*4
print('a number is randomed from 0 to 4 is: ',A)'''
test_seed = int(input("Create a seed number: "))
a=random.seed(test_seed)
print(a)