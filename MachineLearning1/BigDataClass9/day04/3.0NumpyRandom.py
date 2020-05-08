#_*_ coding: utf-8 _*_
# @Time   : 2019/12/4 17:43
# @Author : Z
# @Email  : S
# @File   : 3.0NumpyRandom.py

import numpy as np

n1 = np.random.random((4,4)) # 4行4列随机分布
print(n1)

n2 = np.random.randn(2,4) # 2行4列正态分布
print(n2)

n3 = np.random.uniform(2,4,size=(3,3))  # 3行3列均匀分布
print(n3)

n4 = np.random.chisquare(10,size=(2,3)) # 2行3列卡方分布   自由度越大越趋向于正态分布
print(n4)

n5 = np.random.binomial(10,0.4,size=(4,5))  # 4行5列的二次分布，10次独立不重复实验，发生的概率是0.4，不发生的概率是0.6
print(n5)