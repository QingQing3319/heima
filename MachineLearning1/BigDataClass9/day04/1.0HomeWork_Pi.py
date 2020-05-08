#_*_ coding: utf-8 _*_
# @Time   : 2019/12/4 10:40
# @Author : Z
# @Email  : S
# @File   : 1.0HomeWork_Pi.py
import random
def estimatePi(times):  # 表示的是落入正方形的次数
    hists = 0 # 表示的是落入圆形的次数
    for i in range(times):
        x = random.random() * 2 - 1  # random的结果   [0,1)
        y = random.random() * 2 - 1  # [0,1)*2-1 = [-1,1)
        if x*x+y*y <= 1:
            hists += 1
    return 4*hists/times

if __name__ == '__main__':
    Pi = estimatePi(100000)
    print(Pi)



