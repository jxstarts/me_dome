# coding=gbk
'''
����parseģ��ģ��post����
�����ٶȴʵ�
�������裺
1.��F12
2.�������뵥��girl������ÿ��һ����ĸ��������
3.�����ַ��http//fanyi.baidu.com/sug
4.����NetWork-All-Heardes���鿴������FormData��ֵ��kw:girl
5.��鷵�����ݸ�ʽ�����ַ��ص���json��ʽ����=����Ҫ�õ�json��
'''
from urllib import request, parse
# ������json��ʽ��ģ��
import json
'''
���������ǣ�
1. ����data�������ݡ��ú�URLopen��
2.����һ��json��ʽ�Ľ��
3.�����Ӧ����girl������
'''
basurl = 'https://fanyi.baidu.com/sug'

# �������ģ��form������һ����dict��ʽ
data = {
    # girl �Ƿ��������Ӣ�����ݣ�Ӧ�������û����롤�˴�ʹ��Ӳ����
    "kw": "girl"
}

# ��Ҫʹ��parseģ���data���б���
data = parse.urlencode(data).encode("utf-8")

# ������Ҫ����һ������ͷ������ͷ��Ӧ�����ٰ�����������ݵĳ���
# requestҪ���������ͷ��һ��dict��ʽ

headers = {
    # ��Ϊʹ��post������Ӧ�ð���content-length �ֶ�
    "Content-Length": len(data)
}
# ����headers��data��url���Ϳ��Գ��Է���������

# req = request.Request(basurl, data=data, headers=headers)

rsp = request.urlopen(basurl, data=data)

json_data = rsp.read().decode("utf-8")

# print(json_data)

# ��json �ַ���ת�����ֵ�
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)

for item in json_data['data']:
    print(item['k'], "---", item['v'])