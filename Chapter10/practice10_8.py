# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""
def print_file(filename):
    try:
        with open(filename)as f:
            contents=f.read()
    except FileNotFoundError:
        print(f"Sorry, we can't find the file {filename}.")
    else:
        print(contents)
filenames=['cats.txt','dogs.txt']
for filename in filenames:
    print_file(filename)