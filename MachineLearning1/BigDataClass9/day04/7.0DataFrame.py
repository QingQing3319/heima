#_*_ coding: utf-8 _*_
# @Time   : 2020/1/9 15:17
# @Author : Z
# @Email  : S
# @File   : 7.0DataFrame.py

import pandas as pd
import numpy as np

dict_data = {  'A':1,
               'B':pd.Timestamp('20170426'),
               'C':pd.Series(1,index=list(range(4)),dtype='float32'),
               'D':np.array([3] * 4, dtype='int32'),
               'E':["Python", "java", "C++","C"],
               'F':'ITCast'}

# print(dict_data)

df_obj2 = pd.DataFrame(dict_data)
print(df_obj2)
print(df_obj2*2)  # dataframe每一列乘以2

print("D列所有数据:\n",df_obj2.ix[:,'D'])
print("第2行第E列:\n",df_obj2.ix[1,"E"])
print("第1-3行，D-E列:\n",df_obj2.ix[1:3,"D":"E"])

# loc和iloc方法
print

