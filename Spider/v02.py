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

    html = rsp.read()
    #���� chardet�Զ����
    cs = chardet.detect(html)
    print(cs)

    # ʹ��getȡֵ��֤�������
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)