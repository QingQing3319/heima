#_*_ coding: utf-8 _*_
# @Time   : 2019/11/25 18:00
# @Author : Z
# @Email  : S
# @File   : 2.2list_function.py

list1 = [1,2,3]
list2 = ["apple","pandas"]

#1、cmp(list1, list2):比较两个列表的元素 只有python2中有
# print(cmp(l1,l2))

print("list1的长度:{}".format(len(list1)))

list1.append(list2)
print("在列表末尾添加新的对象：",list1)

list1.extend(list2)
print("用新的列表扩展原来的列表：",list1)

print("统计某元素出现的次数：",list1.count("apple"))

print("在列表中查询某元素的索引值：",list1.index("apple"))

list1.insert(0,"remove")
print("在列表中指定位置插入某值：",list1)

print("删除末尾元素,返回被删除元素：",list1.pop())
print(list1)

list1.remove("apple")
print("列表按元素删除：",list1)

del list1[0]
print("列表按索引删除：",list1)

list1.reverse()
print("列表反转：",list1)

# list1.sort()

