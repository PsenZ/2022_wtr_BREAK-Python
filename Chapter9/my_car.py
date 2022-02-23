# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月16日
"""
# from car import Car
# my_new_car=Car('audi','a4',2019)
# print(my_new_car.get_description())
# my_new_car.odometer_reading=231
# my_new_car.read_odometer()

import car
my_beetle=car.Car('volswagen','beetle',2019)
print(my_beetle.get_description())
my_tesla=car.ElectricCar('tesla','model y',2021)
print(my_tesla.get_description())