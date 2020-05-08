# _*_ coding: utf-8 _*_
# @Time   : 2019/12/5 14:33
# @Author : Z
# @Email  : S
# @File   : 4.0NumpyArray.py

import numpy as np
# 进一步学习矩阵或数组的创建
array1 = np.array([1, 2, 3])
array2 = np.array((1, 2, 3))
array3 = np.array({1, 2, 3})
array4 = np.array({1: 2, 3: 4})
print(type(array4))
print(array1)
print(array2)
print(array3)
print(array4)

# 属性ndim-shape-size
print(array1.ndim)  # 维度
print(array1.shape)  # 形状，几行几列
print(array1.size)  # 有多少个元素

# 二维矩阵
array5 = np.array([[1,2,3],[4,5,6]])  # 有几个中括号，就是几维数组
print(array5)

array6 = np.array([[[1,2,3],[4,5,6],[7,8,9]]],dtype="float32")
print(array6)
print(array6.ndim)  # 3
print(array6.shape) # (1, 3, 3)
print(array6.size)  # 9

print()
# 全为0矩阵
print(np.zeros((3,4), dtype='int64'))
print()

# 全为1矩阵
print(np.ones((4,3),dtype='int64'))
print()

# 等差数列
print(np.linspace(1,10,5,dtype="int64"))
print()

# 等比数列
print(np.logspace(1,10,10,dtype="int64"))
print()

# 对角阵
print(np.diag([2,3,4,5]))