# coding=gbk

'''
����unicode����
'''

import re

hello = "��ã����硣"

pattern = re.compile(r'[\u4e00-\u9fa5]+')

m = pattern.findall(hello)

print(m)