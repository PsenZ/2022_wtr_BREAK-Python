# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月10日
"""
def printPicnic(itemDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))
    for k,v in itemDict.items():
        print(k.ljust(leftWidth,'.')+str(v).rjust(rightWidth))
picnicItems={'sandwiches':4,'apples':12,'cups':3,'cookies':1243}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)