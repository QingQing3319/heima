#_*_ coding: utf-8 _*_
# @Time   : 2019/12/10 14:39
# @Author : Z
# @Email  : S
# @File   : 4.2matrix.py

# matrix是矩阵，一定是2维的，不能够使用matrix定义超过2维度的数据
# mat是matrix的别名
import numpy as np

mat1 = np.matrix(np.random.random(3))
print(mat1)
print(type(mat1))   # numpy.matrixlib.defmatrix.matrix

mat2 = np.matrix([[1,2],[3,4],[3,4]])
print(mat2)

mat3 = np.mat(np.random.randn(3,3))
print(mat3)

# 判定是否可以为3维矩阵
# mat4 = np.mat([[[1,2],[3,4],[3,4]]])   # ValueError: matrix must be 2-dimensional
# print(mat4)

mat5 = np.mat("1,2;3,4;5,6")
print(mat5)