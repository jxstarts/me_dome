# coding=gbk
from urllib import request
'''
ʹ�� urllib.request����һ����ҳ���������ݴ�ӡ����
'''

if __name__ == '__main__':
    url = "https://renren.0717wx.cn/web/index.php?c=miniapp&a=version&do=home&version_id=159"
    # ����Ӧ��url����Ӧҳ����Ϊ����
    rsp = request.urlopen(url)

    # �ѷ��ؽ����ȡ����
    # ��ȡ������������Ϊbytes
    html = rsp.read()

    # ������bytes����ת�����ַ��� ��Ҫ����
    html = html.decode()

    print(html)