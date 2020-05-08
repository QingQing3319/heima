#_*_ coding: utf-8 _*_
# @Time   : 2019/11/20 16:55
# @Author : Z
# @Email  : S
# @File   : 4.0import_from_import.py

#way 1
import math
print(math.sin(0))

#way 2
from math import sin
print(sin(0))

#way 3
from math import sin as f_sin
print(f_sin(0))

# 导入随机数
import numpy as np
print(np.random.random())


