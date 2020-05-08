#_*_ coding: utf-8 _*_
# @Time   : 2019/11/27 16:19
# @Author : Z
# @Email  : S
# @File   : 5.0set.py

# 集合-确定性、无序性、唯一性
set1 = {1,2,32,3,2,1,5,5}
print(set1)

set2 = {1,3,2}
# 集合的增加,set集合是无序的，不存在insert
set2.add(9)
print(set2)

# 集合的删除
set2.remove(9)
print(set2)

# 集合的更新
set2.update({1,2,"huhu","jihuaxi"})
print(set2)

# 集合的运算
set3 = {4,5,6}
set4 = {"hua","cao",4,5}

# 集合的交集
print(set3&set4)
print(set3.intersection(set4))

# 集合的并集
print(set3|set4)
print(set3.union(set4))

# 集合的差集
print(set3-set4)
print(set3.difference(set4))

print(set4-set3)
print(set4.difference(set3))





