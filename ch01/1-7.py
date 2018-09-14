# -*- coding: utf-8 -*- 
# @Time : 2018/9/14
# @Author : virus 
# @File : 1-7.py 
# @Desp : 字典排序


from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])


import json


print(json.dumps(d))
print(d)