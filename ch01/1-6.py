# -*- coding: utf-8 -*- 
# @Time : 2018/9/14
# @Author : virus 
# @File : 1-6.py 
# @Desp : 字典中的键映射多个值

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(2)
print(d)


f = defaultdict(set)
f['a'].add(1)
f['a'].add(2)
f['b'].add(2)
print(f)
