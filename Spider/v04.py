# coding=gbk

from urllib import request, parse
import sys
import io
'''
���ն�url���в�������ķ���
��Ҫʹ��parseģ��
'''

if __name__ == '__main__':

    url = 'http://www.baidu.com/s?'
    wd = input("������:")

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # �ı��׼�����Ĭ�ϱ���
    # Ҫ��ʹ��data�� ��Ҫʹ���ֵ�ṹ
    qs = {
        "wd": wd
    }

    # ת��url����
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # ���ֱ���ÿɶ��Ĵ�������url���ǲ��ܷ��ʵ�
    #fullurl = 'http://www.baidu.com/s?wd=����è'

    rsp = request.urlopen(fullurl)

    html = rsp.read()


    # ʹ��getȡֵ��֤�������
    html = html.decode('utf-8')

    print(html)

