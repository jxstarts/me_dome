# coding=gbk

'''
��ȡ�����Ӱ����
�˽�ajax�Ļ�������
'''

from urllib import request
import json

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"

rsp = request.urlopen(url)
data = rsp.read().decode()

data = json.loads(data)

print(data)