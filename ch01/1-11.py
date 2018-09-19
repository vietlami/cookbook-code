# -*- coding: utf-8 -*- 
# @Time : 2018/9/19
# @Author : virus 
# @File : 1-11.py 
# @Desp : 命名切片

items = [0,1,2,3,4,5,6,7]

a = slice(2,4)

print(items[2:4])
print(items[a])


items[a] = [10,11]

print(items)

del items[a]

print(items)


a = slice(5,50,2)

print(a.start)
print(a.stop)
print(a.step)


s = 'HelloWorld'

a.indices(len(s))

for i in range(*a.indices(len(s))):
    print(s[i])