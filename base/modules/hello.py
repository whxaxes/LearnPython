#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'hello world 模块'

__author__ = 'wanghx'

import sys

def hello():
	args = sys.argv
	if len(args)==1:
		print("hello world")
	else :
		print("hello %s" % args[1])

if __name__ == "__main__":
	hello()