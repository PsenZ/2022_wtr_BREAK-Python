# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月10日
"""

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import pyperclip
text = pyperclip.paste()
# TODO: Separate lines and add stars.
pyperclip.copy(text)
