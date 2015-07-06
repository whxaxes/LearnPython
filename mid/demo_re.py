#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的正则

import re

# match是match一整句
result = re.match(r'^[a-z]+(\d+)[a-z]+$' , 'abcascoa213123kdoa')
print(result)
print(result.group(1))

# 如果想匹配部分则用search
result = re.search(r'\d+' , 'abcascoa213123kdoa')
print(result.group())
