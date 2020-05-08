#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 16:27
# @Author : Z
# @Email  : S
# @File   : 17.1GUI_if_elif_else.py.py
from tkinter import *
import tkinter.messagebox as mb
import tkinter.simpledialog as dl

mb.showinfo("Welcome","Welcome to Guess Number Game")
number = 90

while True:
    # 用户输入猜测数字
    guessNumber = dl.askinteger("GuessGame","Please input your guess number:")

    # 判断
    if guessNumber == number:
        mb.showinfo("WOW","Congratulations, you will win the whole world!")
        break
    elif guessNumber > number:
        mb.showinfo("losser","Guessnumber is larger then given one!")
        continue
    else:
        mb.showinfo("losser","Guessnumber is smaller than given one!")
        continue