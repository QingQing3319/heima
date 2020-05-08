#_*_ coding: utf-8 _*_
# @Time   : 2019/11/29 10:49
# @Author : Z
# @Email  : S
# @File   : 8.0tupleDERIVE.py

# [表达式 for 元素 in 可迭代对象中 if 条件]
# （表达式 for 元素 in 可迭代对象中 if 条件）
# 实现 ： x*x
tuple1 = (x*x for x in range(10))
print(tuple1.__next__())   # 生成器对象具有惰性求值的特点，只在需要时返回元素，比列表推导有更高的效率
print(tuple1.__next__())
print(tuple1.__next__())
print(list(tuple1))
print(list(tuple1))
print(list(tuple1))
