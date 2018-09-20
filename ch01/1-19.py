# -*- coding: utf-8 -*- 
# @Time : 2018/9/20
# @Author : virus 
# @File : 1-19.py 
# @Desp : 转换并同时计算数据


s = ('ACME', 50, 123.45)

print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(s['shares'] for s in portfolio)

print(min_shares)

nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])

print(s)


min_shares = min(portfolio, key=lambda s: s['shares'])

print(min_shares)