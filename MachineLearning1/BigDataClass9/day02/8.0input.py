# _*_ coding: utf-8 _*_
# @Time   : 2019/11/21 15:17
# @Author : Z
# @Email  : S
# @File   : 8.0input.py

# python2的row_input和python3的input用法相同
input1 = input("Please input you age:")
print(input1)
print(type(input1))  # str

input2 = int(input("Please input you age:"))  # int强制转换
print(input2)
print(type(input2))

for i in range(10):
    print(i, end=" ")
