# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月07日
"""
birthdays={'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}
while True:
    print('Enter your name:(blank to quit)')
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for'+name)
        print('What is their birthday?')
        bday=input()
        birthdays[name]=bday
        print('Birthday database updated')