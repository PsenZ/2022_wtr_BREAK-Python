# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月07日
"""
import random
message=['It is certain',
         'It is decidedly so',
         'Yes definitely',
         'Reply hazy try again',
         'Ask again later',
         'concentrate and ask again',
         'my reply is no',
         'outlook not so good',
         'very doubtful']
print(message[random.randint(0, len(message)-1)])
