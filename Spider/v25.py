# coding=gbk

'''
search
'''

import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one12two3asdafsdfasdfsdasdasd56")
print(m.group())

# ���������Ѳ����ʼ��Χ
m = pattern.search("one12two3asdasdfasdfasdfsdasd56", 10, 40)
print(m.group())