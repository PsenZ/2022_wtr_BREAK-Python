# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月14日
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, milage):
        if milage > self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=75):
        self.batter_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.batter_size}-kwh battery.")

    def get_range(self):
        if self.batter_size == 75:
            range = 260
        elif self.batter_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.batter_size != 100:
            self.batter_size = 100


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")


# my_tesla = ElectricCar('Tesla', 'model y', 2022)
# print(my_tesla.get_description())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()


# my_new_car = Car('audi', 'a8', '2021')
# print(my_new_car.get_description())
# my_new_car.odometer_reading = 12345
# my_new_car.read_odometer()
# my_new_car.update_odometer(12000)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(12)
# my_new_car.read_odometer()

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.served_number=0
#
#     def describe_restaurant(self):
#         print(f"The restaurant name is {self.name.title()}")
#         print(f"The cuisine type is {self.type.title()}")
#
#     def open_restaurant(self):
#         print(f"{self.name} is opening")
#
#     def number_served(self):
#         print(f"{self.served_number} people has been served in this restaurant")
#
#     def set_number_served(self,people):
#         self.served_number=people
#
#     def increment_number_served(self,people):
#         self.served_number+=people
# restaurant1=Restaurant('Jack','guangshi')
# restaurant1.describe_restaurant()
# restaurant1.set_number_served(123)
# restaurant1.number_served()
# restaurant1.increment_number_served(10)
# restaurant1.number_served()
