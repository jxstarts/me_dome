# coding=gbk

'''
����һ����ַ
�����Լ���UserAgent����αװ

'''

from  urllib import request,error
import sys,io
if __name__ == '__main__':
    url = "http://www.baidu.com"
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # �ı��׼�����Ĭ�ϱ���
    try:
        # ʹ��head����αװUA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        # req = request.Request(url=url, headers=headers)

        # ʹ��add_header����
        req = request.Request(url=url)
        req.add_header("User-Agent", " Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")

        # ��������
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
