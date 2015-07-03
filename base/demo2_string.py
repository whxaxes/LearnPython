#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python里的字符

# 加r可让字符串不转码
print(r'\r\nasdasdasd')

# '''可以用各种格式字符
print(''' niasdaisdjasd
asdasdasdasddasd
asdasda''')

# ord方法获取字符的ascii码
print(ord('A'))
print(ord('中'))

# chr方法获取ascii对应的字符
print(chr(20013))

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(len('中文'))
print(len(('中文').encode('utf-8')))

# 占位符应用，如果不确定输入字符为什么类型，就可以统一用%s，会将任意类型转成字符串
print('ok,%s' % 'hongxing')
print('HI, %s, you have %d, other test %f %x' % ('wanghx' , 10000 , 2.3 ,254))

print('nihaoa34asda'.replace('34' , ''))

# 字符串切片，用法同list
print('nihaodashuaige'[:5])
