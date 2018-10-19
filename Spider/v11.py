# coding=gbk # Windows下Pycharm中文输出乱码

from  urllib import  request

import sys,io

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')# 读取爬虫数据中文乱码 改变标准输出的默认编码

    url = "http://www.renren.com/965187997/profile"

    rsp = request.urlopen(url)

    html =  rsp.read().decode()

    with open("rsp.html","w",encoding="UTF-8") as f: # 写入文件中文乱码处理
        f.write(html)
