# -*- coding: utf-8 -*- 
# @Time : 2018/9/21
# @Author : virus 
# @File : 2-1.py 
# @Desp : 使用多个界定符分割字符串


line = 'asdf fjdk; afed, fjek,asdf, foo'

import re

print(re.split(r'[;,\s]\s*',line))

fields = re.split(r'(;|,|\s)\s*', line)

print(fields)

values = fields[::2]

delimiters = fields[1::2] + ['']

print(values)
print(delimiters)

''.join(v+d for v, d in zip(values,delimiters))

print(re.split(r'(?:,|;|\s)\s*', line))