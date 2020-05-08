#_*_ coding: utf-8 _*_
# @Time   : 2019/11/29 15:06
# @Author : Z
# @Email  : S
# @File   : 9.0dictDERIVE.py

# {表达式k:v for 元素 in 可迭代对象中 if 条件}
# x:str(x)

dict1 = {x:str(y) for x in range(3) for y in ["zhangsan","lisi","wangwu"]}
print(dict1)