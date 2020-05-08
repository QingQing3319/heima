#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 16:02
# @Author : Z
# @Email  : S
# @File   : ZB.py

from ZA import Arithmatic

# 类-对象
input1 = int(input("Please input your first number:"))
input2 = int(input("Please input your second number:"))
arithmatic = Arithmatic(input1, input2)
print(arithmatic.my_add())
print(arithmatic.my_suf())
print(arithmatic.my_mul())
print(arithmatic.my_div())