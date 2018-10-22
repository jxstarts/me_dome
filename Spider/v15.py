# coding=gbk

from urllib import request, parse

from http import cookiejar



# 创建filecookie的实例

filename = "cookie.txt"

cookie = cookiejar.MozillaCookieJar(filename)

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成HTTPS管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责除此登录
    需要输入用户名面，用来获取cookie凭证
    :return:
    '''

    # 此URL需要从登陆from的action属性中获取
    url = "http://www.renren.com/PLogin.do"
    # 此键值需要从登录from的两个对应input中提取name属性
    data = {
        "email":"13119144223",
        "password":"123456"
    }
    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url, data=data.encode())
    # 使用opener发起请求
    rsp = opener.open(req)

    # 保存cookie到文件
    # ignore_discard表示即使cookie将要被丢弃也要被保存下来
    # ignore_expires表示如果该文件中cookie即使已经过期也要保存下来
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':

    login()

