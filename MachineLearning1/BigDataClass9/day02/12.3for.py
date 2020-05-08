#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 10:58
# @Author : Z
# @Email  : S
# @File   : 12.3for.py

for i in range(10):
    print(i,end=' ')
else:
    print("Done")

for i in [1,2,3,4,5,6,7]:
    print(i,end=' ')

for i in {1,2,3,4,5,6,7}:
    print(i,end=' ')

for i in {"zhangsan":1,"lisi":17}.items():
    print(i,end=' ')