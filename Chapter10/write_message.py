# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月17日
"""
# filename='programming.txt'
# # with open(filename,'w') as file_project:
# #     file_project.write("I love programming.\n")
# #     file_project.write("I love creating new games.\n")
# with open(filename,'a') as file_project:
#     file_project.write("I also love finding meaning in large dataset.\n")
#     file_project.write("I love creating apps that can run ina browser.\n")

filename='guest.txt'
guest=""
while guest!='quit':
    guest = input("Please enter your name:\nEnter 'quit' to end the program\n ")
    if guest!='quit':
        print(f"hello,{guest}")
        with open(filename,'a') as file_object:
            file_object.write(f"{guest}\n")
