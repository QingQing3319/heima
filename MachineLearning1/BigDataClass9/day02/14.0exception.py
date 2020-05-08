#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 11:34
# @Author : Z
# @Email  : S
# @File   : 14.0exception.py

# print(2/0)   #  ZeroDivisionError: division by zero
# hello*5   # NameError: name 'hello' is not defined

try:
    # print(2 / 0)  # ZeroDivisionError: division by zero
    hello * 5
except (ZeroDivisionError,NameError):
    print("div 0 exception or name is not defined")

