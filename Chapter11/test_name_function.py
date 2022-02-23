# -*- coding:utf-8 -*-
"""
作者: 郑沛森
日期: 2022年02月19日
"""
import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'janis joplin')

    def test_first_last_middle_name(self):
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'wolfgang amadeus mozart')
if __name__ == '__main__':
    unittest.main()
