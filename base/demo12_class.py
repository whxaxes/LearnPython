#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的类

# object为要继承的类
class Person(object):
	__slots__ = ('name' , 'age')
	# 公共属性
	situation = 'alive'

	def __init__(self , name , age):
		self.name = name
		self.age = age

	def show_mess(self):
		print("%s's age is %s" % (self.name , self.age))

hx = Person('wanghx' , 24)
ww = Person('wangw' , 26)

hx.show_mess()
ww.show_mess()

print(hx.situation)

# 继承Person类的男人类
class Man(Person):
	def __init__(self , name , age , sex):
		self.name = name
		self.age = age
		# 定义私有变量sex
		self.__sex = sex

# 定义了__len__方法，即可被len()调用
	def __len__(self):
		return 100

	def get_sex(self):
		return self.__sex

	def set_sex(self , value):
		self.__sex = value


hx = Man('wanghx' , 24 , 'male')

hx.show_mess()

# len(xx) 等同于 xx.__len__()
print(len(hx))

print(hx.get_sex())
print(hx.situation)

hx.set_sex('female')

print(hx.get_sex())

print(isinstance(hx , Man))
print(isinstance(hx , Person))

print(hasattr(hx , 'name'))
print(hasattr(hx , '__sex'))


# __slots__变量，用于限制实例添加的属性，该值仅对当前类的实例有效，对子类无效，如果子类继承了父类，那么父类和子类都要有__slots__才有效
class Student(Person):
	__slots__ = ('name' , 'age')

	def __init__(self , name , age):
		self.name = name
		self.age = age

hx = Student('wanghx' , 12)
hx.show_mess()
# 会报错，因为__slots__限定了添加的属性
# hx.score = 'asd'


# @property，给元素做赋值判断
class Student(object):
	@property
	def name(self):
	    return self._name
	
	@name.setter
	def name(self , value):
		if isinstance(value , str) and len(value)>0 and len(value)<10:
			self._name = value
		else :
			raise ValueError('name should be a 0~10 string')

hx = Student()

hx.name = '123'
print(hx.name)
# 会报错，因为上面要求了该值应该为字符串
# hx.name = 123

# 练习
class Screen(object):
	def __check(slef , n):
		if not isinstance(n , int) or n <= 0:
			raise ValueError('value type must be int and bigger than 0')

	@property
	def width(self):
	    return self._width

	@width.setter
	def width(self , value):
		self.__check(value)
		self._width = value

	@property
	def height(self):
	    return self._height

	@height.setter
	def height(self , value):
		self.__check(value)
		self._height = value

	@property
	def resolution(self):
	    return self._width*self._height

ns = Screen()
ns.width = 1000
ns.height = 123
# ns.height = '123'
print(ns.resolution)
	