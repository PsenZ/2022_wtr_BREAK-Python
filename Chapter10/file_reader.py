# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月16日
"""
# with open('pi_digits.txt') as file_object:
#     contents=file_object.read()
# print(contents)
# print(contents.rstrip())

# file_path='E:/郑沛森Python/Python Learning/Chapter10/pi_digits.txt'
# with open(file_path) as file_project:
#     for line in file_project:
#         print(line)

file_name='pi_digits.txt'
with open(file_name) as file_objects:
    lines=file_objects.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
birthday=input("Enter your birthday,in the form mmddyy")
if birthday in pi_string:
    print(f"your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi!")