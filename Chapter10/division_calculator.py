# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月18日
"""
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("you can't divide by zero!")

print("Give me two numbers,and I'll divide them. ")
print("Enter 'q' to quit.")
while True:
    first_number=input("\nFirst number\n")
    if first_number=='q':
        break
    second_number=input("\nLast number\n")
    if second_number=='q':
        break
    try:
         answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
