#_*_ coding: utf-8 _*_
# @Time   : 2019/11/22 16:27
# @Author : Z
# @Email  : S
# @File   : 2.0listOperation.py

# list创建[]
l1 = [1,2,3]

#python2 不用加list  range(8)
l2 = list(range(8))
print(l2)
print(type(l2))

#其他3种数据结构能否转化为list
l3 = list((1,2,3))
print(l3)
print(type(l3))

l4 = list({1,2,3})
print(l4)
print(type(l4))

l5 = list({"zhangsan":2,"lisi":4}.items())
print(l5)

l6 = list({"zhangsan":2,"lisi":4}.values())
print(l6)

# 切片
l7 = list(range(10))
print(l7)
print(l7[1:])
print(l7[:-2])
print(l7[::-1])
print(l7[::2])
print(l7[1::2])