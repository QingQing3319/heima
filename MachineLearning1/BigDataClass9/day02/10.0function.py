#_*_ coding: utf-8 _*_
# @Time   : 2019/11/29 15:17
# @Author : Z
# @Email  : S
# @File   : 10.0function.py

# 参数     返回值
# 没有参数  没有返回值
def SayHi():
    print("hello "*5)
SayHi()

# 有参数  没有返回值
def addThreeBumber(a,b,c):
    print("有参数，没有返回值：{}".format(a+b+c))
addThreeBumber(1,2,3)

# 没有参数  有返回值
def SayHello():
    return "hello "*6
str_hello = SayHello()
print(str_hello)

# 有参数   有返回值
def addNumber(a,b):
    return a+b
str_add = addNumber(3,4)
print("有参数，有返回值：{}".format(str_add))

# 全局变量和局部变量
# 局部变量
m = 20
def printFunction(m):
    print("current m value is:",m)
    m += 80
    print("change m value is:",m)
printFunction(m)
print("Final m value is:",m)

print("---------------")
# 全局变量
n = 30
def printFunction2():
    global n
    print("current n value is:",n)
    n += 100
    print("change n value is:",n)
printFunction2()
print("Final n value is:",n)

