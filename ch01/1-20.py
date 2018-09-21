# -*- coding: utf-8 -*- 
# @Time : 2018/9/20
# @Author : virus 
# @File : 1-20.py 
# @Desp : 合并多个字典或映射

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }


from collections import ChainMap

c = ChainMap(a,b)

print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))


c['z'] = 10
c['w'] = 40

del c['x']

print(a)

values = ChainMap()
values['x'] = 1
print(values)

values = values.new_child()
values['x'] = 2
print(values)

values = values.new_child()
values['x'] = 3
print(values)


print(values['x'])

values = values.parents

print(values)

# 用update()合并字典
a = {'x':1, 'z':3}

b = {'y':2, 'z':4}

merged = dict(b)
merged.update(a)

print(merged['z'])
a['x'] = 13

print(merged['x'])

# 使用chainmap
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4}
merged = ChainMap(a, b)
print(merged['x'])

a['x'] = 42
print(merged['x'])