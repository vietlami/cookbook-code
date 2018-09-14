# -*- coding: utf-8 -*- 
# @Time : 2018/9/14
# @Author : virus 
# @File : 1-8.py 
# @Desp : 字典的运算

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))