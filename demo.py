#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 22:24
# @Author  : 树上老娃娃
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import requests
import parsel
res = requests.get('http://www.baidu.com')
res.encoding=res.apparent_encoding
print(res.status_code)
if res.status_code==200:
    print('连接成功')
    sel = parsel.Selector(res.text)
    wb = sel.xpath('//a/text()').getall()
    print(wb)
else:
    print('网络连接错误')



# print('hello yuan')