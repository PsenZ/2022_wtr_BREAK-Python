# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年01月22日
"""
# # 5.1一个简单示例
# cars=['audi','bmw','benz','lamboghini']
# for car in cars:
#     if cars == 'benz ':
#         print(car.upper())
#     else:
#         print(car.title())

# # 5.2条件测试
# car='audi'
# car.upper()=='audi'
# requested_topping='mushrooms'
# if requested_topping!='anchovies':
#     print("Hold the anchovies")
# banned_users=['andrew','carolina','david']
# user='marie'
# if user not in banned_users:
#     print(f"{user.title()},you can post a response if you wish!")

# age=16
# if age>=18:
#     print("you are old enough to vote")
# else:
#     print("you are not old enough")

# age=12
# if age<4:
#     print("your admission cost is $0.")
# elif age<18:
#     print("your admission cost is $25")
# else:
#     print("your admission cost is $43")

# request_toppings=['mushroom','extra cheese']
# if 'mushroom' in request_toppings:
#     print("Adding mushrooms")
# elif 'pepperoni' in request_toppings:
#     print("Adding pepperoni")
# elif 'extra cheese' in request_toppings:
#     print("Adding extra cheese")
# print("\nFinished making your pizza")

availabe_toppings=['mushroom','olives','green pepper',
                   'pepperoni','pineapples','extra cheese']
request_toppings=['mushroom','french fries','extra cheese']
for request_topping in request_toppings:
    if request_topping in availabe_toppings:
        print(f"Adding {request_topping}")
    else:
        print(f"sorry we dont have {request_topping}")
print("\nFinished making your pizza")