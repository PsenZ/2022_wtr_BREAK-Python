# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月06日
"""
while True:
    print('Who are you?')
    name=input()
    if name!='Joe':
        continue
    print('Hello, Joe. What is the password?(It is a fish.)')
    password=input()
    if password=='swordfish':
        break
print('Access granted.')