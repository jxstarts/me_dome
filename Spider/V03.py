# coding=gbk
'''

����request����ҳ��
�Զ����ҳ�����

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


    # ʹ��getȡֵ��֤�������
    html = html.decode()
    print(type(html))
    # print(html)