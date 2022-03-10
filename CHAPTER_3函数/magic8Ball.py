# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年03月06日
"""
# import random
# def getAnswer(answerNumber):
#  if answerNumber == 1:
#   return 'It is certain'
#  elif answerNumber == 2:
#   return 'It is decidedly so'
#  elif answerNumber == 3:
#   return 'Yes'
#  elif answerNumber == 4:
#   return 'Reply hazy try again'
#  elif answerNumber == 5:
#   return 'Ask again later'
#  elif answerNumber == 6:
#   return 'Concentrate and ask again'
#  elif answerNumber == 7:
#   return 'My reply is no'
#  elif answerNumber == 8:
#   return 'Outlook not so good'
#  elif answerNumber == 9:
#   return 'Very doubtful'
# # r = random.randint(1, 9)
# # fortune = getAnswer(r)
# # print(fortune)
# print(getAnswer(random.randint(1,9)))

# def spam():
#     eggs=99
#     bacon()
#     print(eggs)
# def bacon():
#     ham=101
#     eggs=0
# spam()

def spam():
    global eggs
    eggs='spam'
def bacon():
    egg='bacon'
def ham():
    print(eggs)
eggs=42
spam()
print(eggs)