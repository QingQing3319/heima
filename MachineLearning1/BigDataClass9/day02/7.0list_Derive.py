#_*_ coding: utf-8 _*_
# @Time   : 2019/11/28 14:58
# @Author : Z
# @Email  : S
# @File   : 7.0list_Derive.py

# 列表表达式-求解满足条件的列表-仍然是列表
# 语法：[表达式 for 变量 in 可迭代对象中 if 条件]
# 实践：x*x
list1 = [x*x for x in range(10)]
print(list1)

# 实践1：# 1.使用列表推导式实现嵌套列表的平铺（两个for循环）
vec = [[1,2,3],[4,5],[6,7]]
# 使用列表推导式
list2 = [x for elem in vec for x in elem]
print(list2)
# 等价于
result1 = []
for elem in vec:
    for x in elem:
        result1.append(x)
print(result1)

# 实践2：过滤不符合条件的元素
arr1 = [1,3,-2,5,8,-100]
list3 = [x for x in arr1 if x>0]
print(list3)
# 等价
result2 = []
for x in arr1:
    if x>0:
        result2.append(x)
print(result2)

# 实践3：列表推导中使用多个循环，实现多序列元素任意的组合，并过滤元素
list4 = [(x,y) for x in range(10) for y in range(10) if x!=y]
print(list4)
# 等价
result3 = []
for x in range(10):
    for y in range(10):
        if x!=y:
            result3.append((x,y))
print(result3)

# 实践4：实现列表推导式，实现矩阵转置
vec2 = [[1,2,3],[4,5,6],[7,8,9]]
list5 = [[row[x] for row in vec2] for x in range(3)]
print(list5)

# 等价
result4 = []
for x in range(3):
    result4_son = []
    for row in vec2:
        result4_son.append(row[x])
    result4.append(result4_son)
print(result4)

# zip函数
list_zip = list(zip([1,2,3],[4,5,6],[7,8,9]))
print(list_zip)

# 实践5：使用列表推导生成100以内的所有素数
# 素数-除了1和本身不能被其他数整除的
list6 = [sushu for sushu in range(2,101) if 0 not in [sushu%beichushu for beichushu in range(2,sushu)]]
print(list6)

# 优化
import numpy as np
list7 = [sushu for sushu in range(2,101) if 0 not in [sushu%beichushu for beichushu in range(2,int(np.sqrt(sushu))+1)]]
print(list7)


