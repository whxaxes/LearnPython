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
	last_list = [1]
	while True:
		yield last_list

		new_list = []
		ni = len(last_list)+1
		for j in list(range(ni)):
			if j-1 < 0:
				new_list.append(last_list[0])
			elif j + 1 >= ni:
				new_list.append(last_list[len(last_list)-1])
			else :
				new_list.append(last_list[j-1] + last_list[j])
		last_list = new_list
		
g = triangles()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))