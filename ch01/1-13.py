# -*- coding: utf-8 -*- 
# @Time : 2018/9/19
# @Author : virus 
# @File : 1-13.py 
# @Desp : 通过某个关键字排序一个字典列表

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import  itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))

rows_by_uid = sorted(rows,key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)


rows_by_lfname = sorted(rows,key=itemgetter('fname','lname'))
print(rows_by_lfname)


# lambda 代替

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['fname'],r['lname']))
print(rows_by_fname)
print(rows_by_lfname)


# min() 和max()

print(min(rows, key=itemgetter('uid')))

print(max(rows, key=itemgetter('uid')))