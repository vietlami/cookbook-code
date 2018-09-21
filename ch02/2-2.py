# -*- coding: utf-8 -*- 
# @Time : 2018/9/21
# @Author : virus 
# @File : 2-2.py 
# @Desp : 字符串开头或结尾匹配


filename = 'spam.txt'

print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http://'))


import os
filenames = os.listdir('.')
print(filenames)

print([name for name in filenames if name.endswith(('.txt'))])

# any 如果（）里面所有的元素都为'' 0 False则返回True
any(name.endswith('.py') for name in filenames)

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()



# 切片检查字符串开头结尾
filename = 'spam.txt'

print(filename[-4:] == '.txt')

url = "http://www.python.org"

print(url[:5]=='http:' or url[:6] == 'https:' or url[:4] == 'ftp:')


import re
url = 'http://www.python.org'

re.match('http:|https|ftp:', url)