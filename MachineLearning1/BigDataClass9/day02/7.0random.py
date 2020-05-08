#_*_ coding: utf-8 _*_
# @Time   : 2019/11/21 14:54
# @Author : Z
# @Email  : S
# @File   : 7.0random.py

import random
# 随机数[0,1)
print(random.random())

# 随机数 2-10任意一个
print(random.randint(2,10))

# 随机数 1-10 步长为2 随机奇数
print(random.randrange(1,10,2))

# 将列表随机打乱
x = [1,3,4,5]
random.shuffle(x)
print(x)

import numpy as np
# 生成随机矩阵
print(np.random.randn(3,4))

# 生成均匀分布的随机矩阵
print(np.random.rand(2,3)) # a uniform distribution

