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
    '''
    ������˵�¼
    ��Ҫ�����û����棬������ȡcookieƾ֤
    :return:
    '''

    # ��URL��Ҫ�ӵ�½from��action�����л�ȡ
    url = "http://www.renren.com/PLogin.do"
    # �˼�ֵ��Ҫ�ӵ�¼from��������Ӧinput����ȡname����
    data = {
        "email":"13119144223",
        "password":"123456"
    }
    # �����ݽ��б���
    data = parse.urlencode(data)
    # ����һ���������
    req = request.Request(url, data=data.encode())
    # ʹ��opener��������
    rsp = opener.open(req)

def getHomePage():
    url = "http://www.renren.com/965187997/profile"
    # ����Ѿ�ִ����login��������opener�Զ��Ѿ�������Ӧ��cookieֵ
    rsp = opener.open(url)

    html = rsp.read().decode()

    with open("rsp.html", "w", encoding="utf-8") as f:
        f.write(html)
if __name__ == '__main__':

    login()
    getHomePage()
