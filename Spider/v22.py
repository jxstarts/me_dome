# coding=gbk

'''
ʹ�ò���headers��params
�о����ؽ��

'''
import requests, sys, io
# ��������url������url���ϲ�������
url = "http://www.baidu.com/s?"

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

kw = {
    "wd": "�¶���"

}

headers = {

"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"

}

rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)# ���󷵻���