import numpy as np

def factorial_calculator(number,largest_stored,fact):
    for i in range(largest_stored+1,number+1):
        fact[i] = i * fact[i-1]

fact = np.zeros(10000,dtype=float)
fact[0] = fact[1] = 1

repeat = True 

largest_stored = 1

print('Program to find factorial of a Number')

while repeat :
    number = int(input('Enter an Integer : '))
    if number > largest_stored :
        factorial_calculator(number,largest_stored,fact)
        largest_stored = number
    ans = fact[number]
    print('Factorial of {} is {}'.format(number,ans))
    rep = input('Do you want to Continue (y/n) ?')
    if rep == 'N' or rep == 'n':
        repeat = False   


