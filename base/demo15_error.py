#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的异常捕获

import pdb

try:
	print("try")

	# 打断点
	pdb.set_trace()

	result = 5/0
	print('result:',result)
except ValueError as e:
	print('error except:',e)
except ZeroDivisionError as e:
	print('error except:',e)
finally :
	print('finally')

print("end")

# 抛出错误
raise ValueError('asdasd')

