#_*_ coding: utf-8 _*_
# @Time   : 2019/11/20 16:31
# @Author : Z
# @Email  : S
# @File   : 1.0enconding.py

import sys
print("python3 enconding: 编码", sys.getdefaultencoding())

# 在python3下面使用encode和decode来进行编码和解码
str="传智播客"
# utf-8：unicode transform format 8 bytes（将unicode编码转换为字节码）
print(str.encode()) # b'\xe4\xbc\xa0\xe6\x99\xba\xe6\x92\xad\xe5\xae\xa2'

print(b'\xe4\xbc\xa0\xe6\x99\xba\xe6\x92\xad\xe5\xae\xa2'.decode()) # 传智播客

# encode()的默认编码为utf-8 ，decode()的默认编码为utf-8
print(str.encode().decode())

# 用什么编码，就用什么解码
print(str.encode('gbk'))  # b'\xb4\xab\xd6\xc7\xb2\xa5\xbf\xcd'
print(str.encode('gbk').decode('gbk'))  # 传智播客

# unicode编码转为中文
print(str.encode('unicode_escape').decode('unicode_escape'))


