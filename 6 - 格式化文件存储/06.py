# coding=gbk
import xml.etree.ElementTree as et

# ���ڴ��д���һ���յ��ĵ�


etree = et.ElementTree()

e = et.Element('Student')

etree._setroot(e)

e_name = et.SubElement(e, 'Name')
e_name.text = "hahahah"


etree.write('06.xml')
