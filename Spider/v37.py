# coding=gbk

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import sys, io,time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # ��ȡ���������������� �ı��׼�����Ĭ�ϱ���

# ������Ҫ�ֶ����·��
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url=url)

text = driver.find_element_by_id('wrapper').text

print(text)

print(driver.title)
# ��ҳ����
driver.save_screenshot('index.png')

# id "kw"�ǰٶȵ���������ǵõ�������UIԪ�غ�ֱ�����롱����è��

driver.find_element_by_id('kw').send_keys(u"����è")

# id = "su"�ǰٶ������İ�ť��clickģ����
driver.find_element_by_id('su').click()

time.sleep(5)

driver.save_screenshot("daxiongmao.png")

# ��ȡ��ǰҳ���cookie
print(driver.get_cookies())

# ģ��������������Ctrl+A
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# CTRL+X
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u"��ĸ")
driver.save_screenshot('hangmu.png')
driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('hangmu2.png')

# ��������clear
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

# �ر������
driver.quit()