# coding=gbk

import requests
import sys, io
url = "http://www.baidu.com"
# 两种请求方式
# 使用get请求
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
rsp = requests.get(url=url)
print(rsp.text)

# 使用request请求
rsp = requests.request("get", url=url)
print(rsp.text)