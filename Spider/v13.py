# coding=gbk

from urllib import request, parse

from http import cookiejar


# ����cookie��ʵ��
cookie = cookiejar.CookieJar()

# ���� cookie�Ĺ�����
cookie_handler = request.HTTPCookieProcessor(cookie)

# ����http���������
http_handler = request.HTTPHandler()

# ����HTTPS������
https_handler = request.HTTPSHandler()

# �������������
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    return None


if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"

