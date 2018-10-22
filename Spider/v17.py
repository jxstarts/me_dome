# coding=gbk

from urllib import request
# 导入Python ssl处理模块
import ssl

import io,sys

# 利用非认证上下文环境替换认证的上下文环境
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.12306.cn/mormhweb"

rsp = request.urlopen(url=url)

html = rsp.read().decode()

print(html)