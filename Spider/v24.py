# coding=gbk

'''
������Match��ʹ�ð���
'''
import re

# ��������ֳ��������飬 ��С����Ϊ��λ
s = r'([a-z]+)([a-z]+)'
pattern = re.compile(s,re.I)# s.I��ʾ���Դ�Сд

m = pattern.match("Hello world wide web")
# group(0)��ʾ����ƥ��ɹ��������ַ���
s = m.group(0)
print(s)

a = m.span(0)# ����ƥ��ɹ��������ַ����Ŀ��
print(a)

# group(1)��ʾ����ƥ��ɹ��ĵ�һ���ַ���
s = m.group(1)
print(s)

a = m.span(1)# ����ƥ��ɹ��ĵ�һ���ַ����Ŀ��

s = m.groups()# �ȼ���m.group(1), m.group(2)..........
print(s)