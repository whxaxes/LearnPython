#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python里的迭代器

# 字符迭代
a = ''
for s in 'nihaodashuaige':
	a += s+','
print(a)


# 字典的迭代 同 js
dictory={'name':'hongxing' , 'age':18}
for k in dictory:
	print(k,'=',dictory[k])


# 判断对象是否为可迭代
from collections import Iterable
print(isinstance('abc' , Iterable))
print(isinstance({} , Iterable))
print(isinstance(123 , Iterable))


# 模拟js里的for(var i=0;i<xx;i++){}
new_list = list(range(8))
for i,value in enumerate(new_list):
	if i>5:
		print(value)

for x,y in [(1,2),(3,4)]:
	print(x+y)