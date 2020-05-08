#_*_ coding: utf-8 _*_
# @Time   : 2019/12/12 11:03
# @Author : Z
# @Email  : S
# @File   : 4.5any_all_unique.py

import numpy as np

arr1 = np.array([[1,3,2],[3,2,4],[5,9,-6]])
print(arr1)

print(np.any(arr1>0))
print(np.all(arr1>0))

# unique函数
print(np.unique(arr1)) # sorted unique  去重排序
print(np.unique(arr1,return_counts=True))