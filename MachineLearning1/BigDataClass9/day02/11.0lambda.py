#_*_ coding: utf-8 _*_
# @Time   : 2019/12/2 17:46
# @Author : Z
# @Email  : S
# @File   : 11.0lambda.py

# 匿名函数 lambda 变量名：表达式
lam1 = lambda m,n,k:m+n+k
print(lam1(1,2,3))

lam2 = lambda m,n,k=0:m+n+k
print(lam2(1,4))

print((lambda m,n,k=0:m+n+k)(1,4))

# 在map函数中使用lambda函数
print(list(map(lambda x:x*x,range(10))))

# map使用
def myAdd(a,b):
    return a+b
print(list(map(myAdd,range(5),range(5))))

# reduce函数-累计求和
from functools import reduce
print(reduce(myAdd,range(10)))
