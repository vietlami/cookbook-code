# -*- coding: utf-8 -*- 
# @Time : 2018/9/21
# @Author : virus 
# @File : 2-3.py 
# @Desp : 用Shell通配符匹配字符串

from fnmatch import  fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))

print(fnmatch('foo.txt', '?oo.txt'))

print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

print([name for name in names if fnmatch(name, 'Dat*.csv')])

# fnmatch()在不同的系统 大小写敏感程度不一

# 为了区别可以使用 fnmatchcase()

print(fnmatchcase('foo.txt', '*.TXT'))

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]


print([addr for addr in addresses if fnmatchcase(addr, '* ST')])

print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])