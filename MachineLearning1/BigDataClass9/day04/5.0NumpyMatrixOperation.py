#_*_ coding: utf-8 _*_
# @Time   : 2019/12/12 11:16
# @Author : Z
# @Email  : S
# @File   : 5.0NumpyMatrixOperation.py

import numpy as np

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[1,2],[3,4]])

# 矩阵的乘法-第一个矩阵的列的维度和第二个矩阵的行的维度必须一致
print(arr1.dot(arr2))
print(np.dot(arr1,arr2))
# [[ 7 10]
#  [15 22]]

# 矩阵的行列式
from numpy.linalg import det,inv,qr,eig,svd
print("arr1 matrix values is:",det(arr1))  # 正对角相乘减去副对角相乘
# 矩阵的逆-存在的条件是矩阵的行列式不为0
print("arr1 inverse values is:",inv(arr1))
arr3 = np.array([[1,2],[2,4]])
print(det(arr3))  # arr3的行列式为0
# print(inv(arr3))  # numpy.linalg.linalg.LinAlgError: Singular matrix

# 矩阵的分解--qr分解--将矩阵分解成q矩阵和r矩阵
from numpy.linalg import qr

q,r = qr(arr3)  # 将arr3分解成q矩阵和r矩阵
print(q)
print(r)
arr3 = np.dot(q,r)  # 将分解后的q矩阵和r矩阵还原成arr3
print("qr还原：",arr3)


# 特征值和特征向量-----PCA
from numpy.linalg import eig

eigenvalues,eigenvectors = eig(arr3)
print(eigenvalues)
print(eigenvectors)

# vec * val对角阵 * vec的逆   -----> 将分解后的特征值和特征向量还原成arr3
print("PCA还原：",np.dot(eigenvectors,np.dot(np.diag(eigenvalues),inv(eigenvectors))))

# 奇异值分解    svd
from numpy.linalg import svd
U,Sigma,VT = svd(arr3)
print("U:",U)
print("Sigma:",Sigma)
print("VT:",VT)

# 还原
arr3 = np.dot(U,np.dot(np.diag(Sigma),VT))
print("svd还原：",arr3)


