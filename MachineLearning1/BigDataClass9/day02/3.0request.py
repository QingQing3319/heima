#_*_ coding: utf-8 _*_
# @Time   : 2019/11/20 16:48
# @Author : Z
# @Email  : S
# @File   : 3.0request.py

import requests

response = requests.get("https://www.baidu.com")
print(response.encoding) # ISO-8859-1
print(response.text)
print(response.url) # https://www.baidu.com/

