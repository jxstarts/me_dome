# coding=gbk

'''
search
'''

import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one12two3asdafsdfasdfsdasdasd56")
print(m.group())

# 参数表明搜查的起始范围
m = pattern.search("one12two3asdasdfasdfasdfsdasd56", 10, 40)
print(m.group())