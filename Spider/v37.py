# coding=gbk

from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import sys, io,time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 读取爬虫数据中文乱码 改变标准输出的默认编码

# 可能需要手动添加路径
driver = webdriver.Chrome()

url = "http://www.baidu.com"

driver.get(url=url)

text = driver.find_element_by_id('wrapper').text

print(text)

print(driver.title)
# 网页快照
driver.save_screenshot('index.png')

# id "kw"是百度的输入框，我们得到输入框的UI元素后直接输入”大熊猫“

driver.find_element_by_id('kw').send_keys(u"大熊猫")

# id = "su"是百度搜索的按钮，click模拟点击
driver.find_element_by_id('su').click()

time.sleep(5)

driver.save_screenshot("daxiongmao.png")

# 获取当前页面的cookie
print(driver.get_cookies())

# 模拟输入两个按键Ctrl+A
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# CTRL+X
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

driver.find_element_by_id('kw').send_keys(u"航母")
driver.save_screenshot('hangmu.png')
driver.find_element_by_id('su').send_keys(Keys.RETURN)

time.sleep(5)
driver.save_screenshot('hangmu2.png')

# 清空输入框，clear
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

# 关闭浏览器
driver.quit()