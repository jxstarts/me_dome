# coding=gbk

'''
破解有道词典

'''

from urllib import request, parse

def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    data = {
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "1540188153180",
        "sign": "c7ffc4ff5159b7cd5dcea065a834a05f",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
        "typoResult": "false"
    }

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    handers = {

        "Accept": "application/json,text/javascript,*/*;q = 0.01",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "201",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-862125489@10.169.0.83;JSESSIONID=aaaipvux6Ovlz4xDmwAAw;OUTFOX_SEARCH_USER_ID_NCOO = 373533485.789991;___rl__test__cookies = 1540188153176",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent":"Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.67Safari / 537.36",
    }

    req = request.Request(url=url, handers=handers)

    rsp = request.urlopen(req)

    html = rsp.read.decode()

    print(html)

if __name__ == '__main__':

    youdao("gril")