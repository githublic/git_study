#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 22:24
# @Author  : 树上老娃娃
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import requests
res = requests.get('http://www.baidu.com')
print(res.status_code)
if res.status_code==200:
    print('连接成功')
# print('hello yuan')