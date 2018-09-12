# -*- coding: utf-8 -*- 
# @Time : 2018/9/12
# @Author : virus 
# @File : 1-3.py 
# @Desp : 保留最后 N 个元素


from collections import deque

# 得到一个固定长度为3的队列
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

# 得到无限队列
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
# 在队列前端插入
q.appendleft(4)
print(q)
# 在队列后端弹出元素
q.pop()
print(q)
# 在队列前端弹出元素
q.popleft()
print(q)