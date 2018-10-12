# coding=gbk
from urllib import request
'''
使用 urllib.request请求一个网页，并把内容打印出来
'''

if __name__ == '__main__':
    url = "https://renren.0717wx.cn/web/index.php?c=miniapp&a=version&do=home&version_id=159"
    # 打开相应的url把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来类容类型为bytes
    html = rsp.read()

    # 如果想把bytes内容转换成字符串 需要解码
    html = html.decode()

    print(html)