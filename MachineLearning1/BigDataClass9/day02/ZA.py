#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 16:02
# @Author : Z
# @Email  : S
# @File   : ZA.py

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