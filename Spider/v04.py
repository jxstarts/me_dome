# coding=gbk

from urllib import request, parse
import sys
import io
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''

if __name__ == '__main__':

    url = 'http://www.baidu.com/s?'
    wd = input("请输入:")

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
    # 要想使用data， 需要使用字典结构
    qs = {
        "wd": wd
    }

    # 转换url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 如果直接用可读的带参数的url，是不能访问的
    #fullurl = 'http://www.baidu.com/s?wd=大熊猫'

    rsp = request.urlopen(fullurl)

    html = rsp.read()


    # 使用get取值保证不会出错
    html = html.decode('utf-8')

    print(html)

