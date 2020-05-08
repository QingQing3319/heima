#_*_ coding: utf-8 _*_
# @Time   : 2019/11/26 10:29
# @Author : Z
# @Email  : S
# @File   : 3.0tuple.py

# 只有一个元素的tuple
tuple1 = (100,)
print(tuple1)
print(type(tuple1))

# 如果tuple中存在list部分
tuple2 = (1,2,3,["pandas","numpy"])
print(tuple2)
print(tuple2[3])
print(tuple2[3][0])

tuple2[3].append("de")
print(tuple2)

tuple2[3][0] = "pear"
print(tuple2)

# 各个数据类型之间的转换
tuple3 = tuple([1,2,3])
print(tuple3)

tuple4 = tuple({1,2,3,4})
print(tuple4)

tuple5 = tuple({"apple":1,"pandas":2}.items())
print(tuple5)

#切片操作
tuple6 = tuple(range(10))
print(tuple6)

print(tuple6[::-1])
print(tuple6[2:8:2])
print(tuple6[0:4])

# list---->tuple   冻结
# tuple--->list   解冻

# 多元素赋值-序列解包
a,b = 1,2
print(a,b)

v = (3,4)
(c,d) = v
print(c,d)
