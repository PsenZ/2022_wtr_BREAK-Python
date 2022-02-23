# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月16日
"""
from car import Car,ElectricCar
my_bettle=Car('volkswagen','beetle',2018)
print(my_bettle.get_description())
my_tesla=ElectricCar('tesla','model x',2021)
print(my_tesla.get_description())