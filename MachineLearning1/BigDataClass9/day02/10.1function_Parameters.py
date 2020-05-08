#_*_ coding: utf-8 _*_
# @Time   : 2019/12/2 15:05
# @Author : Z
# @Email  : S
# @File   : 10.1function_Parameters.py

# 默认参数
# def sayHello(name="zhangsan",age):    #  有默认值的参数需写在无默认值的参数之后
def sayHello(name,age=11):
    print("name is：{}, age is {}".format(name,age))
sayHello("zhangsan")
sayHello("zhangsan", 22)

# 关键字参数
def addThreeNumber(m,n,q):
    print(m+n+q)
addThreeNumber(m=11,n=22,q=33)
addThreeNumber(11,22,q=33)
addThreeNumber(11,22,33)

print("---------")
#VarArgs参数 --->  * tuple    ** dict
def printFunction(fparameters,*tuple_1,**dict_1):
    print(fparameters)
    print(tuple_1)
    print(dict_1)
printFunction(1,2,3,4,2,1,name="zhangsan",lisi="huahua")





