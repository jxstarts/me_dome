# coding=gbk

'''

findall
'''
import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 adsasda  666  5255  asdasd")
print(s)

s = pattern.finditer("i am 18 adsasda  666  5255  asdasd")
print(type(s))

for i in s:
    print(i.group())
