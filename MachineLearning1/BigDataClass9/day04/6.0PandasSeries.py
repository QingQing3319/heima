#_*_ coding: utf-8 _*_
# @Time   : 2019/12/17 10:19
# @Author : Z
# @Email  : S
# @File   : 6.0PandasSeries.py

# Series是一维数组结构
import pandas as pd
print(pd.Series([1,2,3,4]))
series1 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
print("series:",series1)
print("series1.head:",series1.head(2))
print("series.ndim:",series1.ndim)
print("series1.shape:",series1.shape)
print("series1.size:",series1.size)
print("series1.index:",series1.index)  # Index(['a', 'b', 'c', 'd'], dtype='object')
print("series1.values:",series1.values) # [1 2 3 4]
print("series1.dtype:",series1.dtype)

# 字典适合构建series
dict1 = dict(zip(["zhangsan", "lisi", "wangwu"], [22, 44, 33]))
dict2 = pd.Series(dict(zip(["zhangsan", "lisi", "wangwu"], [22, 44, 33])))
print(dict1)
print()
print(dict2)

# 查看series的值
print(dict2['zhangsan'])
print(dict2['lisi'])

print(dict2.value_counts()) # 值的词频统计
print(dict2.unique()) # 值去重


