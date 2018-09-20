# -*- coding: utf-8 -*-
# @Time : 2018/9/20
# @Author : virus 
# @File : 1-16.py 
# @Desp : 过滤序列元素

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 列表推导过滤序列元素
lista = [n for n in mylist if n > 0]

listb = [n for n in mylist if n<0]

print(list(lista))
print(list(listb))

# 使用内建函数filter()过滤序列元素
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int,values))

print(ivals)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

import math

# 过滤的时候转换数据
print(list([math.sqrt(n) for n in mylist if n > 0]))


# 不符合条件的用新值代替
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)


# 用另外一个相关联的序列来过滤某个序列
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]

print(more5)

print(list(compress(addresses,more5)))