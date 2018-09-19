# -*- coding: utf-8 -*- 
# @Time : 2018/9/19
# @Author : virus 
# @File : 1-12.py 
# @Desp : 序列中出现次数最多的元素

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)

top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])


# 手动增加计数
morewords = ['why','are','you','not','looking','in','my','eyes']

for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])


# or

word_counts = Counter(words)

word_counts.update(morewords)


# 计算

a = Counter(words)
b = Counter(morewords)

print(a)
print(b)

print(a - b)
print(a + b)