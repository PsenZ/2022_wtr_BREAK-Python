# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""
import json
numbers=[2,3,5,7,11,13]
filename='number.json'
with open(filename,'w') as f:
    json.dump(numbers,f)