#_*_ coding: utf-8 _*_
# @Time   : 2019/12/3 11:19
# @Author : Z
# @Email  : S
# @File   : 13.0fileOperation.py

def writeFile():
    content = """\
This is jupyter!
This is Anaconda!
This is MachineLearning!\
"""
    file1 = open("sen.txt", mode="w")
    file1.write(content)
    file1.close()

def readFile():
    file2 = open("sen.txt", mode="r")
    while True:
        line = file2.readline()
        print(line, end="")

        if len(line) == 0:
            file2.close()
            break



if __name__=="__main__":
    # writeFile()
    readFile()
