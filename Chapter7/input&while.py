# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月06日
"""

# message=input("Tell me something,and I will repeat it back to you:")
# print(message)

# name=input("Please enter your name:")
# print(f"\nHello,{name}")

# prompt="If you tell us who you are, we can personalize the messages you see."
# prompt+="\n What's your first name?"
# name=input(prompt)
# print(f"\nHello,{name}")

# age=input("How old are you?")
# print(age)

# height=input("How tall are you,in inches?")
# height=int(height)
# if height>=48:
#     print("\nyou are tall enough to ride.")
# else:
#     print("\nyou'll be able to ride when you are a little older.")

# car=input("what kind of car do you need?")
# print(f"\nLet me see if I can find you a {car}")

# seat=input("how many people for meal ?")
# seat=int(seat)
# if seat>8:
#     print("There is no avilable table")
# else:
#     print("OK follow me")

# current_number=1
# while current_number<=5:
#     print(current_number)
#     current_number+=1


# prompt="\nTell me something,and I will repeat it back to you: "
# prompt+="\nEnter 'quit' to end this program"
#
# message=""
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         print(message)


# prompt="\nTell me something,and I will repeat it back to you: "
# prompt+="\nEnter 'quit' to end this program"
# active=True
# while active:
#     message=input(prompt)
#     if message=='quit':
#         active=False
#     else:print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to the {city.title()}")


# current_number=0
# while current_number<10:
#     current_number+=1
#     if current_number%2==0:
#         continue
#     print(current_number)

# x=1
# while x<=100:
#     print(x)

# unconfirmed_users = ['alice', 'brain', 'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#     print(f"Veriyfying user:{current_users.title()}")
#     confirmed_users.append(current_users)
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets :
#     pets.remove('cat')
# print(pets)

responses={}
polling_active=True
while polling_active:
    name=input("\n what is your name?")
    response=input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(Yes/No)")
    if repeat=='No':
        polling_active=False
print("\n---Poll Results---")
for name ,response in responses.items():
    print(f"{name} would like to climb {response}")