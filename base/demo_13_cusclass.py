#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的定制类

class Looper(object):

	def __init__(self):
		self.a = 0

# print()的时候回调用该方法
	def __str__(self):
		return "Looper Object"

# 直接在控制台输入对象名回车时会调用repr方法
	__repr__ = __str__

# 有了这个属性即可以使用for in
	def __iter__(self):
		return self

# 每次for in的时候都会调用该next方法
	def __next__(self):
		self.a += 1
		if self.a > 50:
			# 停止Iterator
			raise StopIteration()

		return self.a


lo = Looper()

print(lo)

for k in lo:
	print(k)