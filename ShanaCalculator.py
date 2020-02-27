#!/usr/bin/env python3.8
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2
   
print('please pick an operation:')
print('1.addition')
print('2.subtraction')
print('3.multiply')
print('4.division')

choice = input('enter a choice(1/2/3/4): ')

num1 = float(input('enter first number: '))
num2 = float(input('enter another: '))

if choice == '1':
    print(num1, "+", num2, "=", addition(num1,num2))

elif choice =='2':
    print(num1, "-", num2, "=", subtraction(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", division(num1,num2))

else:
    print('invalid input')





