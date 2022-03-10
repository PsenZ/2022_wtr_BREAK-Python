# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月06日
"""
# print('Enter the name of cat 1:')
# catName1 = input()
# print('Enter the name of cat 2:')
# catName2 = input()
# print('Enter the name of cat 3:')
# catName3 = input()
# print('Enter the name of cat 4:')
# catName4 = input()
# print('Enter the name of cat 5:')
# catName5 = input()
# print('Enter the name of cat 6:')
# catName6 = input()
# print('The cat names are:')
# print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)

catsName=[]
while True:
    print('Enter the name of cat'+str(len(catsName)+1)+'(enter nothing to stop.):')
    name=input()
    if name=='':
        break
    catsName=catsName+[name]
print('The cat name are:')
for name in catsName:
    print(''+name)