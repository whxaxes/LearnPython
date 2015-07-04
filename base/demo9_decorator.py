#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的装饰器decorator

def log(func):
	def wrapper(*args , **kw):
		print('call %s()'%func.__name__)
		return func(*args , **kw)
	return wrapper

# 等同于now = log(now)
@log
def now():
	print("2015-7-4")

# 此时由于now = wrapper，所以now.__name__已经变成wrapper
# 解决办法是添加@functools.wraps(func)，效果等同于wrapper.__name__ = now.__name__
print(now.__name__)

now()

import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args , **kw):
			print('%s %s()'% (text , func.__name__))
			return func(*args , **kw)
		return wrapper
	return decorator

# 等同于now = log('go')(now)
@log('go')
def now():
	print("2015-7-4")

# 
print(now.__name__)

now()

# 练习,编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
# 同时既可以@log('go')也可以@log
def log(arg):
	def inner(func , arg):
		@functools.wraps(func)
		def wrapper(*args , **kw):
			print('begin %s %s()' % (arg , func.__name__))
			result = func(*args , **kw)
			print('end %s %s()' % (arg , func.__name__))
			return result
		return wrapper

	if isinstance(arg , str):
		def decorator(func):
			return inner(func , arg)
		return decorator
	else :
		return inner(arg , 'call')

@log('go')
def now():
	print("2015-7-4")

now()

@log
def now():
	print("2015-7-4")

now()

