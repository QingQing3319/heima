#_*_ coding: utf-8 _*_
# @Time   : 2019/12/4 15:03
# @Author : Z
# @Email  : S
# @File   : 2.0conv.py

# 定义卷积
import scipy as sp
print(sp.convolve([1,2,3,4],[4,5,6]))  # 一维卷积运算 [6,5,4] 进入[1,2,3,4] 相交的部分相乘再相加
# [ 4 13 28 43 38 24]




