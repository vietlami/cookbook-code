# -*- coding: utf-8 -*- 
# @Time : 2018/9/12
# @Author : virus 
# @File : 1-1.py 
# @Desp : 解压序列赋值给多个变量

p = (4,5)

x,y = p


print(x)
print(y)


data = ["ACME",50,91.1,(2018,9,12)]

name,shares,price,date = data

print(name)
print(shares)
print(price)
print(date)

name,shares,price,(year,mon,day) = data

print(year)
print(mon)
print(day)