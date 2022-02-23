# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""
import json
filename='username.json'
with open(filename) as f:
    username=json.load(f)
    print(f"Welcome back,{username}")