#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python黑科技，屌屌的列表生成 

print(list(range(5 , 15)))

print([x*x for x in range(1 , 11)])

print([x*x for x in range(1 , 11) if x%2==0])

print([x+y for x in range(1 , 11) for y in range(1 , 11)])
print([x+y for x in 'abc' for y in 'abc'])

my_dict = {'fi':'asdasd' , 'bi':'123123'}
print([k+'='+v for k,v in my_dict.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L = ['Hello', 'World', 1818 , 'IBM', 'Apple' , None]
print([s.lower() for s in L if isinstance(s , str)])


# generator，改[]为()

g = (s.lower() for s in L if isinstance(s , str))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# 通过yield创建genrator
def looper():
	i = 0
	while i<10:
		yield i
		print('ll')
		i+=2
g = looper()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


# 杨辉三角
def triangles():
	L = [1]
	while True:
		yield L
		L = [1]+[L[j-1] + L[j] for j in list(range(1 , len(L)))]+[1]
		
g = triangles()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 更简洁的杨辉三角
# zip方法：for i in zip([0,1,2,1] , [1,2,1,0]) ==> i ==> [0,1],[1,2],[2,1],[1,0]
# sum方法是求list里的所有值的和，结果即上面的[0+1 , 1+2 , 2+1 , 1+0]
def triangles():
	L = [1]
	while True:
		yield L
		L = [sum(i) for i in zip([0]+L , L+[0])]

# 迭代器
from collections import Iterable
from collections import Iterator

print(isinstance([] , Iterable))
print(isinstance([] , Iterator))

# iter方法可以把Iterable转化成Iterator
print(isinstance(iter([]) , Iterator))

print(isinstance(g , Iterator))

ng = iter('abcd')
print(next(ng))
print(next(ng))
print(next(ng))
print(next(ng))
