# coding=gbk

from lxml import etree

# ֻ�ܶ�ȡxml���ݣ�HTML����
html = etree.parse("./v30.html")

rst = etree.tostring(html, pretty_print=True)

print(rst)