# coding=gbk

'''
ʹ�ô�����ʰٶ���վ

'''
from urllib import request, error
import sys,io

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # �ı��׼�����Ĭ�ϱ���
    url = "http://www.baidu.com"

    # ���ô������ʹ�ò��裺

    # 1.���ô����ַ
    proxy = {'http': '39.135.24.12:80'}
    # 2.����ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3.����Opener
    opener = request.build_opener(proxy_handler)
    # 4.��װOpener
    request.install_opener(opener)

    # �����������url����ʹ�ô��������
    try:
        rsp = request.urlopen(url=url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)