#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python map reduce filter sorted

def db(x):
	return x*x

def beStr(x):
	return str(x)

print(list(map(db , [1,2,3,4])))
print(list(map(beStr , [1,2,3,4,'ss'])))

# reduce方法需要引入
from functools import reduce

def fn(x , y):
	return x*10 + y

# reduce的执行就是fn(fn(fn(1 , 2) , 3) , 4)
print(reduce(fn , [1,2,3,4]))

# 字符串formate
def normalize(str):
	return str[0].upper() + str[1:].lower()

L = ['adam', 'LISA', 'barT']
print(list(map(normalize , L)))

# 乘积函数
def prod(l):
	def cj(x,y):
		return x*y
	return reduce(cj , l)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# filter
L = ['asd' , '' , None , 'asdasd' , 1123]
def gl(x):
	return x and isinstance(x , str)
print(list(filter(gl , L)))

# 练习
def is_palindrome(n):
	n = str(n)
	l = len(n)//2
	return (not l) or n[:l] == n[len(n)-l:][::-1]
print(list(filter(is_palindrome , list(range(1000)))))


# sorted
# key为传入函数，reverse为是否翻转
print(sorted(['bob', 'about', 'Zoo', 'Credit'] , key=str.lower , reverse=True))

# lambda 为匿名函数
print(sorted(['bob', 'about', 'Zoo', 'Credit'] , key=lambda x:len(x) , reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 按照姓名排序
print(sorted(L , key=lambda x:x[0]))
# 按照分数排序
print(sorted(L , key=lambda x:x[1] , reverse=True))