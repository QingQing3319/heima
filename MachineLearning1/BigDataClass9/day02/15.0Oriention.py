#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 11:45
# @Author : Z
# @Email  : S
# @File   : 15.0Oriention.py

class Arithmatic(object):
    def __init__(self,x,y):
        self.new_x = x
        self.new_y = y

    def my_add(self):
        return self.new_x+self.new_y

    def my_suf(self):
        return self.new_x-self.new_y

    def my_mul(self):
        return self.new_x*self.new_y

    def my_div(self):
        return self.new_x/self.new_y

# 类-对象
input1 = int(input("Please input your first number:"))
input2 = int(input("Please input your second number:"))
arithmatic = Arithmatic(input1, input2)
print(arithmatic.my_add())
print(arithmatic.my_suf())
print(arithmatic.my_mul())
print(arithmatic.my_div())
