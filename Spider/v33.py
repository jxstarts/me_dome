# coding=gbk

from urllib import request
from bs4 import BeautifulSoup
import sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # �ı��׼�����Ĭ�ϱ���

url = "http://www.baidu.com"

rsp = request.urlopen(url=url)

content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs �Զ�ת��
content = soup.prettify()

print(content)