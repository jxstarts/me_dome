# coding=gbk
'''

利用request下载页面
自动检测页面编码

'''
import chardet
import urllib
if __name__ == '__main__':
    url = "https://renren.0717wx.cn/web/index.php?c=miniapp&a=version&do=home&version_id=159"

    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    html = rsp.read()

    print("url:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))


    # 使用get取值保证不会出错
    html = html.decode()
    print(type(html))
    # print(html)