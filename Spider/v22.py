# coding=gbk

'''
使用参数headers和params
研究返回结果

'''
import requests, sys, io
# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

kw = {
    "wd": "新东方"

}

headers = {

"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"

}

rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)# 请求返回码