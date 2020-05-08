#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 11:43
# @Author : Z
# @Email  : S
# @File   : 14.1exception_while_break_if_elif_else.py.py

number = 90

while True:
    try:
        # 用户输入猜测数字
        guessNumber = int(input("Please input your guess number:"))

        # 判断
        if guessNumber == number:
            print("WOW")
            print("Congratulations, you will win the whole world!")
            break
        elif guessNumber > number:
            print("Guessnumber is larger then given one!")
            continue
        else:
            print("Guessnumber is smaller than given one!")
            continue
    except:
        print("error:input again")