# coding=gbk

from urllib import request
# ����Python ssl����ģ��
import ssl

import io,sys

# ���÷���֤�����Ļ����滻��֤�������Ļ���
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # �ı��׼�����Ĭ�ϱ���

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.12306.cn/mormhweb"

rsp = request.urlopen(url=url)

html = rsp.read().decode()

print(html)