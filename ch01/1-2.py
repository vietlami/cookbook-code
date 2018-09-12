# -*- coding: utf-8 -*- 
# @Time : 2018/9/12
# @Author : virus 
# @File : 1-2.py 
# @Desp : 解压可迭代对象赋值给多个变量


record = ('Anna',"Anna@example.com",'773-555-1212','847-555-1212')
# 分解记录
name,email,*phone_numbers = record

print(name)
print(email)
print(phone_numbers)

*trailing,current = [10,8,7,1,9,5,10,3]
# 分解记录

print(trailing)
print(current)


records = [
    ('foo',1,2,3),
    ('bar', 'hello'),
    ('foo',3,4,5)
]

def do_foo(x,y,z):
    print('foo',x,y,z)

def do_bar(s):
    print('bar',s)

for tag, *args in records:
    if tag == 'foo':
        print(args)
        do_foo(*args)
    elif tag == 'bar':
        print(args)
        do_bar(*args)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# 字符切割

line_arr = line.split(":")

# 分解
uname, *fields, homedir, sh = line_arr

# 输出
print(uname,fields,homedir,sh)


# 解压后丢弃 可以用_或者ign

record = ('ACME',50,123.45,(12,9,2018))

name, *_, (*_, year) = record

# 输出

print(name,year)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
