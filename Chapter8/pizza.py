# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月14日
"""


def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
