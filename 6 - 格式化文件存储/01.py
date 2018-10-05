# coding=gbk
import xml.dom.minidom

# �������xml�ļ�
from  xml.dom.minidom import parse

# ʹ��minidom��xml�ļ�
DOMTree = xml.dom.minidom.parse("Student.xml")
# �õ��ĵ�����
doc = DOMTree.documentElement

# ��ʾ��Ԫ��
for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("------Node:{0}-------".format(ele.nodeName))
        childs = ele.childNodes
        for child in childs:
            if child.nodeName == "Name":
                # data ���ı��ڵ��һ�����ԣ���ʾ����ֵ
                print("Name:{0}".format(child.childNodes[0].data))
            if child.nodeName == "Age":
                # data ���ı��ڵ��һ�����ԣ���ʾ����ֵ
                print("Age:{0}".format(child.childNodes[0].data))
                if child.hasAttribute("detail"):
                    print("Age-detail:{0}".format(child.getAttribute("detail")))
            if child.nodeName == "Mobile":
                # data ���ı��ڵ��һ�����ԣ���ʾ����ֵ
                print("Mobile:{0}".format(child.childNodes[0].data))
