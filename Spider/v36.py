# coding=gbk

'''
ͨ��WebDriver�����ٶȽ������ݲ���
'''

from selenium import webdriver
import time

# ͨ��keysģ�����
from selenium.webdriver.common.keys import Keys

# �����Ǹ��������һ��ʵ��
# �Զ����ջ�������������Ӧ�������
driver = webdriver.PhantomJS()

# ��������û������Ӧ������������Ҫָ�������λ��

driver.get("http://www.baidu.com")


# ͨ����������title��ǩ
print("Title:{0}".format(driver.title))