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

print(content)