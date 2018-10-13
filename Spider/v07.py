# coding=gbk

'''
URlError的使用

'''
from urllib import request, error
import sys, io
if __name__ == '__main__':

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
    url = "http://www.baidu.com"

    try:
        req = request.Request(url=url)
        rsp = request.urlopen(req)
        html = rsp.read().decode("utf-8")
        print(html)
    except error.URLError as e:
        print("URLError:{0}".format(e.reason))
        print("URLError:{0}".format(e))
    except Exception as e:
        print(e)
