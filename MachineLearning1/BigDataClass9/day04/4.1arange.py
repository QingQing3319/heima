#_*_ coding: utf-8 _*_
# @Time   : 2019/12/10 14:30
# @Author : Z
# @Email  : S
# @File   : 4.1arange.py

import numpy as np

print(np.arange(10))
print(np.arange(2,11,1))
arr1 = np.arange(10).reshape(2,5)
print(arr1)
print(arr1.ndim)
print(type(arr1))