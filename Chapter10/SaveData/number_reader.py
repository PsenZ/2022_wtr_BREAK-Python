# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""
import json
filename='number.json'
with open(filename) as f:
    numbers=json.load(f)
print(numbers)