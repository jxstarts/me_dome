# coding=gbk
import requests #������Ҫ�İ�
import json

search = input("��������Ҫ���������:")

url = "https://fanyi.baidu.com/extendtrans" #����ĵ�ַ
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36"} #���������ͷ��

#�����ύ������
posData={"query":search,
                "from":"en",
                "to":"zh"}

response = requests.post(url=url,data=posData,headers=headers)#ģ������

#��ȡresponse��������2�ַ�ʽ һ����text��ȡ��ֱ�����ı���ʽ ���ǿ��������� ��Ҫ�ֶ�����response.encoding("����") �������
#����һ�־���response.content ����������վֱ�ӷ��ص����� �����Ƹ�ʽ Ȼ��ͨ��decode���뼴��
#��Ϊ���ص���json�����������ǽ����������ַ�������json��ʽת�� ʹ��json.loads()����ת��
json_data=json.loads(response.content.decode())

#Ȼ�����ǿ���ͨ����ʽ�����߽���json�Ľ���
print("����:{0} ����:{1}".format(search,json_data["data"]["st_tag"]))