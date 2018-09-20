# -*- coding: utf-8 -*- 
# @Time : 2018/9/20
# @Author : virus 
# @File : 1-18.py 
# @Desp : 映射名称到序列元素


# 通过名称来访问元素

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('jonesy@example.com','2012-10-19')

print(sub)

print(sub.addr)

print(sub.joined)

print(len(sub))

addr,joined = sub

print(addr)

print(joined)


# 改变命名元组的值

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
s = Stock('ACME', 100, 123.45)
print(s)
s = s._replace(shares=75)
print(s)


# 填充数据


Stock = namedtuple('Stock',['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}

print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}

print(dict_to_stock(b))