# coding=gbk

from selenium import  webdriver

import sys, io


# ������Ҫ�ֶ����·��
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url=url)

text = driver.find_element_by_id('wrapper').text

print(text)
