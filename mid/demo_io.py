#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的IO、文件操作

f = open('./test.txt' , 'r')

value = f.read()

f.close()

# 更简洁的写法，即添加其他参数
with open('./test.txt' , 'r') as f:
	print(f.read())

# 写文件
with open('./test.txt' , 'w') as f:
	f.write("你好，OK OK")

import os

npath = os.path.abspath('.')
print(npath)

print(os.path.join(npath , 'newfile'))

print(os.path.split(r'\nihao\nini\abs.txt'))
print(os.path.splitext(r'\nihao\nini\abs.txt'))

print(os.listdir("."))
# 列出py文件
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])