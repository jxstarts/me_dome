# coding=gbk

from urllib import request
from bs4 import BeautifulSoup
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码

url = "http://www.baidu.com"

rsp = request.urlopen(url=url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())
print("=="*20)
titles = soup.select("title")
print(titles[0])
print("=="*20)
metas = soup.select("meta[content='always']")
print(metas[0])
print("=="*20)
