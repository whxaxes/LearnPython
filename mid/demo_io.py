#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的IO、文件操作

f = open('./test.txt' , 'r')

value = f.read()

f.close()

# 更简洁的写法，即添加其他参数
with open('./test.txt' , 'r' , encoding='utf-8') as f:
	print(f.read())

# 写文件
with open('./test.txt' , 'w' , encoding='utf-8') as f:
	f.write("你好，OK OK")

import os

npath = os.path.abspath('.')
print(npath)

print(os.path.join(npath , 'newfile'))

# 分割文件名
print(os.path.split(r'\nihao\nini\abs.txt'))
# 分割文件后缀名
print(os.path.splitext(r'\nihao\nini\abs.txt'))
# 列出当前目录下的文件
print(os.listdir("."))
# 列出py文件
print([x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


# 获取目录下所有文件
def getAllDir(p):
	if not os.path.exists(p):
		return []

	nL = os.listdir(p)
	for k in nL:
		np = os.path.join(p , k)
		if os.path.isdir(np):
			nL += getAllDir(np)
			
	return nL

print(getAllDir(r"E:\个人项目\GitHub\canvas-test\src\Game-demo"))
