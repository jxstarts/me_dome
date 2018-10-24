# coding=gbk

from lxml import etree

# ֻ�ܶ�ȡxml���ݣ�HTML����
html = etree.parse("./v30.html")

rst = html.xpath('//book')
print(type(rst))
print(rst)

# xpath����˼�ǣ�����category����ֵΪsport��bookԪ��
rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)

# xpath����˼�ǣ�����category����ֵΪsport��bookԪ���µ�yearԪ��
rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)