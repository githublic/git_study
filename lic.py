#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 22:04
# @Author  : 树上老娃娃
# @Site    : 
# @File    : lic.py
# @Software: PyCharm
from lxml import  etree
import requests
import csv
fp=open('D://JHW/doubanbook.csv','wt',newline='',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))
#构造url
urls=['http://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like  Gecko) Chrome/53.0.2785.143 Safari/537.36'
           }
for url in urls:
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//tr[@class="item"]')
    for info in infos:
        name=info.xpath('td/div/a/@title')[0]
        url=info.xpath('td/div/a/@href')[0]
        book_infos=info.xpath('td/p/text()')[0]
        author=book_infos.split('/')[0]
        publisher=book_infos.split('/')[-3]
        date=book_infos.split('/')[-2]
        price=book_infos.split('/')[-1]
        rate=info.xpath('td/div/span[2]/text()')[0]
        comments=info.xpath('td/p/span/text()')
        comment=comments[0] if len(comments) !=0 else '空'
        writer.writerow((name,url,author,publisher,date,price,rate,comment))
fp.close()