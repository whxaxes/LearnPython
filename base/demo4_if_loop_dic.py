#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python里的条件判断、循环、字典

a = 30

if a:
	print(a)
elif a>=30:
	print(a*2)
else:
	print(False)

array = [1,2,3,4,6,7,8,9]
for x in array:
	print(x)

alen = len(array)
while alen:
	alen -= 1
	print(array[alen])


# 字典
names = ['wanghx','zhaoritian','dagb']
value = [123 , 456 , 789]
dictory = {}
i=0
while i<len(names):
	dictory[names[i]] = value[i]
	i += 1

print(dictory)

# 同js的in
print('wanghx' in names)
print('wanghx' in dictory)

# 直接用[]获取，如果key不存在dict中，会报错，用get则不会报错，返回None
print(dictory['wanghx'])
print(dictory.get('wanghx'))
print(dictory.get('wanghxaa'))

# dict删除元素
dictory.pop('zhaoritian')
print(dictory)


# set
s1 = set([1,2,3])
s1.add(4)
s1.add(4)
s1.remove(1)
print(s1)