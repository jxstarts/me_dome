# coding=gbk

from urllib import request, parse

from http import cookiejar


# 创建cookie的实例
cookie = cookiejar.CookieJar()

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成HTTPS管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    return None


if __name__ == '__main__':
    url = "http://www.renren.com/965187997/profile"

