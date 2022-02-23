# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""


def get_formatted_name(first, last,middle="" ):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name=f"{first} {last}"
    return full_name
