#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 10:53
# @Author : Z
# @Email  : S
# @File   : 12.1while_if_elif_else.py

number = 90
flag = False

while flag == False:
    # 用户输入猜测数字
    guessNumber = int(input("Please input your guess number:"))

    # 判断
    if guessNumber == number:
        print("WOW")
        print("Congratulations, you will win the whole world!")
        flag = True
    elif guessNumber > number:
        print("Guessnumber is larger then given one!")
    else:
        print("Guessnumber is smaller than given one!")


