# -*- coding: utf-8 -*- 
# @Time : 2018/9/14
# @Author : virus 
# @File : 1-9.py 
# @Desp : 查找两字典的相同点

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())


c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)