# coding=gbk

from urllib import request, parse

from http import cookiejar


# ����cookie��ʵ��
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# ���� cookie�Ĺ�����
cookie_handler = request.HTTPCookieProcessor(cookie)

# ����http���������
http_handler = request.HTTPHandler()

# ����HTTPS������
https_handler = request.HTTPSHandler()

# �������������
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    # ����Ѿ�ִ����login��������opener�Զ��Ѿ�������Ӧ��cookieֵ
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp.html", "w", encoding="utf-8") as f:
        f.write(html)
if __name__ == '__main__':

    getHomePage()

