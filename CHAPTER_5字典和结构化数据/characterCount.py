# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月07日
"""
message='It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)
    count[character]+=1
print(count)
