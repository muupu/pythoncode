#-*- coding: UTF-8 -*-

### test enumerate ###
str = 'abcdefgh'
for i, c in enumerate(str):
	print i, c

### test dict.setdefault###
# D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
# 如果k不在字典中，就将k作为键值添加到字典D中，并且value值为d
# 如果键在字典中，返回这个键所对应的值。如果键不在字典中，向字典 中插入这个键，并且以default为这个键的值，并返回 default。
d = {'A': 95, 'B': 75, 'C': 85}
print d
print d.setdefault('C', 123) # 返回85
print d
print d.setdefault('D', 123) # 返回123
print d