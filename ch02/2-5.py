# -*- coding: utf-8 -*- 
# @Time : 2018/9/30
# @Author : virus 
# @File : 2-5.py 
# @Desp : 字符串搜索和替换

text = 'yeah. but no, bunt yeah, but no, but yeah'

res = text.replace('yeah', 'yep')

print(res)

text = 'Today is 09/30/2018. pycon start 3/13/2013'

# sub()函数 第一个参数是被匹配的模式，第二个参数是替换模式。 反斜杠数字比如\3指前面模式
# 的捕获组号
import re
res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

print(res)


# 提升性能，提前编译

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
res = datepat.sub(r'\3-\1-\2',text)

print(res)


# 使用替换回调函数

from calendar import month_abbr

def change_date(m):
    mom_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mom_name,m.group(3))

res = datepat.sub(change_date,text)

print(res)

# 发生多少替换
newtext, n = datepat.subn(r'\3-\1-\2', text)

print(newtext,"\n", n)
