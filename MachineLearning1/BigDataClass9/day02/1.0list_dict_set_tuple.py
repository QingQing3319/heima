#_*_ coding: utf-8 _*_
# @Time   : 2019/11/22 10:38
# @Author : Z
# @Email  : S
# @File   : 1.0list_dict_set_tuple.py

#1、list列表-异质数据，有序，根据下标进行查询
#1.1、list创建
list1 = [2,3,4,"zhangsan",[3,5,6]]
print(list1)
print(type(list1))

#1.2、list查询
print(list1[0])
print(list1[4][0])
print()

#1.3、list增加元素
list1.append((2,2,2)) # 添加至末尾
print(list1)

list2 = ["lisi","wangwu"]
list1.append(list2)
print("list1.append(list2):{}".format(list1))

list1.extend(list2)
print("list1.extend(list2):{}".format(list1))
print()

list1.insert(0,(4,4))
print("list1.insert:{}".format(list1))

#1.4、list删除元素
list1.remove(2)
print(list1)

del list1[2:]
print(list1)

#1.5、list修改元素
list1[1] = "修改元素"
print(list1)

#1.6、list删除列表
del list1

#2、dict字典-无序类型的、通过key查询数据的数据结构
#2.1、dict创建
dict1 = {"a":1,"b":2,3:"c"}
print(dict1)
print(type(dict1))

#2.2、dict查询
print(dict1["a"])

#2.3、dict增加元素
dict1["d"]="hu"
print(dict1)

#2.4、dict删除元素
del dict1["a"]
print(dict1)

#2.6、dict修改元素
dict1["b"] = "aaaa"
print(dict1)

#2.5、dict删除字典
del dict1

#3、set集合
#3.1、set创建
set1 = {1,2,3,4}
print(set1)
print(type(set1))

#3.2、set查询
#3.3、set增加元素
#3.4、set删除元素
#3.5、set删除列表
#3.6、set修改元素

#4、tuple元组-异质数据，有序，根据下标进行查询，元素一旦确定，不能进行删除、更新、修改等操作
#4.1、tuple创建
tuple1 = (1,2,3,"huahua")

#4.2、tuple查询
print(tuple1[3])

#4.3、tuple增加元素 元组不可增加元素
#4.4、tuple删除元素 元组不可删除元素
#4.5、tuple删除元组
del tuple1
# print(tuple1)

#4.6、tuple修改元素 元组不可被修改


