# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年01月22日
"""
# alien_0={'color':'green','points':5}
# # new_points=alien_0['points']
# # print(f"you just earned {new_points} points")
# print(alien_0)
# alien_0['x_position']=0
# alien_0['y_position']=25
# print(alien_0)

# alien_0={}
# alien_0['color']='green'
# alien_0['points']=5
# print(alien_0)

# alien_0={'color':'green'}
# print(f"the alien is {alien_0['color']}.")
# alien_0['color']='yellow'
# print(f"the alien is now {alien_0['color']}.")

# alien_0={'x_position':0,'y_position':25,'speed':'medium'}
# alien_0['speed']='fast'
# print(f"Original x_position:{alien_0['x_position']}.")
# if alien_0['speed']=='slow':
#     x_increment=1
# elif alien_0['speed']=='medium':
#     x_increment=2
# else:
#     x_increment=3
# alien_0['x_position']=alien_0['x_position']+x_increment
# print(f"New x_position is :{alien_0['x_position']}")

# alien_0={'color':'green','points':5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favorite_languages={
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
# }
# language=favorite_languages['phil'].title()
# print(language)

# alien_0={'color':'green','speed':'slow','points':5}
# point_values=alien_0.get('points','no point value assigned.')
# print(point_values)

# use_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in use_0.items():
#     print(f"\nKey:{key}")
#     print(f"\nValue:{value}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")
# if 'eren' not in favorite_languages:
#     print("eren, please take our poll")

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# alien = [alien_0, alien_1, alien_2]
# for aliens in alien:
#     print(aliens)

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:4]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"Total number of aliens:{len(aliens)}")

# pizza={
#     'crust':'thick',
#     'toppings':['mushrooms','extra cheese'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza"
#       " with following toppings:")
# for topping in pizza['toppings']:
#     print("\t"+topping)

# favorite_languages={
#     'jen':['python','ruby'],
#     'sarah':['c'],
#     'edward':['ruby','haskell'],
#     'phil':['python','haskell'],
# }
# for name,languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
# for username, user_info in users.items():
#     print(f"\nUsername:{username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name:{full_name.title()}")
#     print(f"\tLocation:{location.title()}")

cities = {
    'Paris': {
        'Country': 'france',
        'Population': 100000000,
        'facts': 'wine',
    },
    'New York': {
        'Country': 'USA',
        'Population': 200000000,
        'facts': 'supreme',
    },
    'Beijing': {
        'Country': 'China',
        'Population': 300000000,
        'facts': 'tiananmen',
    },
}
for city, city_info in cities.items():
    print(f"\nCity:{city}")
    country = city_info['Country']
    population = city_info['Population']
    fact = city_info['facts']
    print(f"\tCountry:{country}")
    print(f"\tPopulation:{population}")
    print(f"\tfacts:{fact}")
