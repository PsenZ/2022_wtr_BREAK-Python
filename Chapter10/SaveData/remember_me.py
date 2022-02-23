# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""
import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name?")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_stored_username()
    check=input(f"{username},Is this username correct?(Y/N)")
    if check=='Y':
        if username:
            print(f"Welcome back,{username}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back,{username}")
    # try:
    #     with open(filename) as f:
    #         username = json.load(f)
    # except FileNotFoundError:
    #     username=input("What's your name. ")
    #     with open(filename, 'w') as f:
    #         json.dump(username, f)
    #         print(f"We'll remember you when you come back,{username}")
    # else:
    #     print(f"Welcome,{username}")


greet_user()
