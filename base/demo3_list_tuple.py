#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python里的list 和 tuple


# list，就是js里的数组
my_list = ['wanghx' , 'zhaoritian' , 'dagb' , 'xiaogb']

print('This is list :',my_list,'and list\'s length is',len(my_list))

print(my_list[1])
# 输出最后一个值
print(my_list[-1])
# 输出倒数第二个值
print(my_list[-2])

# list添加值
my_list.append('whatthefuck')
# 插入
my_list.insert(1 , 'jacky')
print(my_list)

# 删除最后一个
my_list.pop()
# 删除第一个
my_list.pop(0)
print(my_list)
# 排序
my_list.sort()
print('排序后',my_list)

# 切片
my_list = list(range(10))
print(my_list)
print('切片：',my_list[1:3])
print('切片：',my_list[-3:])
print('切片（每隔两个取一个）：',my_list[1:6:2])

# 通过切片复制list
new_list = my_list[:]
new_list.append(10)
print(my_list)
print(new_list)

# tuple 跟list一样，但是初始化后不能更改，获取元素的方法跟list一样，但是没有append、insert，pop方法
my_tuple = ('wnaghx' , 'zhaoritian' , 'dagb')

print(my_tuple[1])
print(my_tuple[-1])

# 定义只有一个元素的tuple，如果无逗号则当成字符
singleTuple = ('nihao' , )
print(singleTuple)


listtuple = ('asdasd' , '111' , ['nihao' , '333'])

listtuple[2].append('nihhh');

print(listtuple)
