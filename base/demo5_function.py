#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python里的函数

import math

# 十六进制转换
print(hex(255))

# 绝对值函数
def my_abs(x):
	# 判断x的类型，如果不是整型或浮点类型则抛出错误
	if not isinstance(x , (int , float)):
		raise TypeError('wrong type')

	if x >= 0 :
		return x
	else:
		return -x

print(my_abs(-5))
print(my_abs(5))

# 定义一个空函数
def noop():
	pass

# 使用math的方法，定义一个求斜边的工时，x，y默认值为1
def xiebian(x=1 , y=1):
	return math.sqrt(math.pow(x, 2) + math.pow(y,2))

print(xiebian(5))
print(xiebian(5 , 6))


# 定义默认值，两次调用方法，引用的都是同个l
def add_end_1(l = []):
	l.append('END')
	return l

print(add_end_1())
print(add_end_1())

# 解决办法
def add_end_2(l = None):
	if l is None:
		l = []
	l.append('END')
	return l

print(add_end_2())
print(add_end_2())

# 参数
# *num说明可以传入list或者tuple
def getresult(*num):
	a = 0
	for i in num:
		a += i;
	return a

print(getresult(1,2,3,4))

# **dic传入格式为xxx=xxx，会自动转成字典
def getresult(key , **dic):
	if not 'name' in dic:
		return 'no name'

	return key,dic

print(getresult('asd' , name='wanghx' , sex='male'))
print(getresult('asd' , sex='male'))

# *作为特殊分隔符
def getresult(arg1 , arg2 , * , name='wanghx' , sex):
	return arg1,arg2,name,sex

(a , b , c , d) = getresult(1 , 2 , sex='male')
print(c,d)
print(getresult(1 , 2 , sex='male'))


# 汉诺塔
def move(n, a, b, c):
	if n == 1:
		print('move', a, '-->', c)
	else :
		move(n-1, a, c, b)
		move(1, a, b , c)
		move(n-1, b, a, c)	

move(3, 'A', 'B', 'C')
