# 动态HTML


## 爬虫跟反爬虫

## 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从JavaScript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面
    
## Selenium + PhantomJS
- Selenium：web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium==2.48.0
    - 官网：http://selenium-python.readthedocs.io/index.html
    - Windows下安装教程：https://www.cnblogs.com/yjlch1016/p/8463765.html
- PhantomJs(幽灵)
    - 基于webkit的无界面的浏览器
    - 官网：http://phantomjs.org/download.html
    - Windows下安装教程：https://blog.csdn.net/kobe111_/article/details/81568862
- Selenium 库有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例v36
- chrome + chromedriver
    - 下载安装Chrome：下载+安装
    - 下载安装chromedriver
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例37