# coding=gbk # Windows��Pycharm�����������

from  urllib import  request

import sys,io

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')# ��ȡ���������������� �ı��׼�����Ĭ�ϱ���

    url = "http://www.renren.com/965187997/profile"

    rsp = request.urlopen(url)

    html =  rsp.read().decode()

    with open("rsp.html","w",encoding="UTF-8") as f: # д���ļ��������봦��
        f.write(html)
