# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月07日
"""
# def egg(someParameter):
#     someParameter.append('Hello')
# spam=[1,2,3]
# egg(spam)
# print(spam)

# spam = ['apples', 'bananas', 'tofu', 'cats']
# spam[-1] = 'and ' + spam[-1]  # 将最后一个值加上‘and ’
# print(', '.join(spam))


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
for j in range(6):
    for i in range(9):
        print(grid[i][j], end='')
    print()
