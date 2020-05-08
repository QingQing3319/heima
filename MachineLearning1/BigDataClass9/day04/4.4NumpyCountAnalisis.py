#_*_ coding: utf-8 _*_
# @Time   : 2019/12/10 16:53
# @Author : Z
# @Email  : S
# @File   : 4.4NumpyCountAnalisis.py

#   np.mean(), np.sum()：所有元素的平均值，所有元素的和，参数是 number 或 array
# 	np.max(), np.min()：所有元素的最大值，所有元素的最小值，参数是 number 或 array
# 	np.std(), np.var()：所有元素的标准差，所有元素的方差，参数是 number 或 array
# 	np.argmax(), np.argmin()：最大值的下标索引值，最小值的下标索引值，参数是 number 或 array
# 	np.cumsum(), np.cumprod()：返回一个一维数组，每个元素都是之前所有元素的 累加和 和 累乘积，参数是 number 或 array

import numpy as np
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)

# 行求和
print(np.sum(arr1,axis=1))
# 列求和
print(np.sum(arr1,axis=0))

# 行求均值
print(np.mean(arr1,axis=1))

# 列求均值
print(np.mean(arr1,axis=0))

# 行最大，最小值
print(np.max(arr1, axis=1))
print(np.min(arr1,axis=1))

# 列最大，最小值
print(np.max(arr1,axis=0))
print(np.min(arr1,axis=0))

# 标准差（列）
print(np.std(arr1,axis=0))

# 方差（列）
print(np.var(arr1,axis=0))

# 最大最小值下标索引(列)
print(np.argmax(arr1,axis=0))
print(np.argmin(arr1,axis=0))

# 每个元素之前元素的累加和& 累加积(列)
print(arr1)
print(np.cumsum(arr1,axis=0))
print(np.cumprod(arr1,axis=0))