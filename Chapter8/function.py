# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月08日
"""


# def greet_user():
#     print("hello")
#
#
# greet_user()

# def greet_user(username):
#     print(f"Hello,{username.title()}")
# greet_user('mike')

# def describe_pet(animal_type,pet_name):
#     print(f"\n I have a {animal_type}")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}")
# describe_pet(animal_type='lion',pet_name='jack')

# def favorite_book(author, book_name):
#     print(f"One of my favorite books is {author.title()}'s {book_name.title()}")
# favorite_book('alice', 'wonderland')


# def get_formatted_name(first_name, last_name,middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', middle_name='lee', last_name='hendrix')
#
# print(musician)
# musician = get_formatted_name('jack', 'lick')
# print(musician)

# def build_person(first_name,last_name,age=None):
#     person ={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#     return person
# musician=build_person('jack','henderix',age=18)
# print(musician)

# def get_formatted_name(first_name,last_name):
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     print("\n(enter 'q' at any time to quit)")
#     f_name=input("First name:")
#     if f_name=='q':
#         break
#     l_name=input("Last name:")
#     if l_name=='q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print(f"\nHello,{formatted_name}")

# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# unprinted_designs=['phone case','robot pendant','dodecahedron']
# completed_models=[]
# while unprinted_designs:
#     current_design=unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append((current_design))
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def make_pizza(*toppings):
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(*toppings):
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

# def make_pizza(size,*toppings):
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(16,'pepperoni')
# make_pizza(23,'mushrooms','green peppers','extra cheese')

# def build_profile(first,last,**user_info):
#     user_info['first_name']=first
#     user_info['last_name']=last
#     return user_info
# user_profile=build_profile('albert','einstein',
#                            location='princeton',
#                            field='physics')
# print(user_profile)

# def build_car(manufactor,type,**manu):
#     manu['manufactors']=manufactor
#     manu['types']=type
#     return manu
# car_profile=build_car('subaru','outback',
#                       color='blue',
#                       tow_package='Ture')
# print(car_profile)

def make_pizza(size,*toppingS):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppingS:
        print(f"-{topping}")