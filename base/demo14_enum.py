#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的枚举类，用宏定义一些全局变量

from enum import Enum,unique

Month = Enum('Month' , ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.__members__)

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)


# unique装饰器用于保证无重复值
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.__members__)
print(Weekday(1))
print(Weekday.Mon)
print(Weekday.Mon.value)