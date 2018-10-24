# coding=gbk

from urllib import request
from bs4 import BeautifulSoup
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码

url = "http://www.baidu.com"

rsp = request.urlopen(url=url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs 自动转码
content = soup.prettify()

# print(content)

# print("==" *20)
# print(soup.head)
# print("==" *20)
# print(soup.meta)
# print("==" *20)
# print(soup.link)
# print(soup.link.name)
# print(soup.link.attrs)
# print(soup.link.attrs['type'])
# soup.link.attrs['type'] = 'hahahah'
# print(soup.link)
#
# print("==" *20)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.attrs)
# print(soup.title.string)
#
# print("==" *20)
# print(soup.name)
# print(soup.attrs)
# print(soup.name)

# print(soup.name)
#
# print("*" *30)
# for node in soup.head.contents:
#     if node.name == "meta":
#         print(node)
#     if node.name == "title":
#         print(node.string)
# print("*" *30)

import re
print("*" * 30)
# tags = soup.find_all(name='meta')
tags = soup.find_all(re.compile('^me'), content="always")
for tag in tags:
    print(tag)
print("*" * 30)
