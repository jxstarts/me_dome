# coding=gbk

from selenium import  webdriver

import sys, io


# 可能需要手动添加路径
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url=url)

text = driver.find_element_by_id('wrapper').text

print(text)
