#_*_ coding: utf-8 _*_
# @Time   : 2019/11/26 14:58
# @Author : Z
# @Email  : S
# @File   : 4.0dict.py

# 定义
dict1 = {"apple":1,"pear":2}
print(dict1)

# zip函数
dict2 = dict(zip(["hadoop","spark"],[3,4]))
print(dict2)

# dict函数
dict3 = dict(huahua=44, hujiao=55)
print(dict3)

# 字典的删除
# del dict3
# print(dict3)

# 字典的清空
dict3.clear()
print(dict3)

# 字典中的key必须是有hash值的类型---这种类型必须是不可变的类型---tuple
# print(hash([1,2,3])) #TypeError: unhashable type: 'list'
print(hash((1,2,3)))

# dict4 = dict(zip([["zhangsan","huhu"],"lisi"],[18,22]))
# print(dict4) # TypeError: unhashable type: 'list'

dict4 = dict(zip([("shanxi","hebei"),"hunan"],[3,4]))
print(dict4)

# key不能重复
dict5 = {"a":1,"b":3,"a":77}
print(dict5)