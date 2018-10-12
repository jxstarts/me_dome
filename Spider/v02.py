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

    html = rsp.read()
    #利用 chardet自动检测
    cs = chardet.detect(html)
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)