# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月06日
"""
# import random
# secretNumber=random.randint(1,20)
# print('I am thinking of a number between 1 and 20.')
# for guessesTaken in range(1,7):
#     print('Take a guess.')
#     guess=int(input())
#     if guess<secretNumber:
#         print('Your guess is too low.')
#     elif guess>secretNumber:
#         print('Your guess is too high.')
#     else:
#         break
# if guess==secretNumber:
#     print('Good job! You guessed my number in '+str(guessesTaken)+' guesses!')
# else:
#     print('Nope. The number I was thinking of was '+str(secretNumber))

# def collatz(number):
#     if number%2==0:
#         return number/2
#     else:
#         return (number*3)+1
# number=int(input())
# num=collatz(number)
# while num!=1:
#     number=int(input())
#     collatz(number)

def collatz(number):
    if number % 2 == 0:
        return number // 2

    elif number % 2 == 1:
        return 3 * number + 1


while True:
    try:
        number = int(input('Please enter Arabic numerals: '))
    except ValueError:
        print("Invalid string in input! You can only enter Arabic numerals!\n")
        continue

    print(collatz(number))

    if collatz(number) != 1:
        continue
    else:
        break
