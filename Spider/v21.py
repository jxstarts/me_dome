# coding=gbk

import requests
import sys, io
url = "http://www.baidu.com"
# ��������ʽ
# ʹ��get����
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
rsp = requests.get(url=url)
print(rsp.text)

# ʹ��request����
rsp = requests.request("get", url=url)
print(rsp.text)