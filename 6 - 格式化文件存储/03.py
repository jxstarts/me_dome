# coding=gbk
import xml.etree.ElementTree as et

tree = et.parse("Student.xml")

root = tree.getroot()

for e in root.iter('Name'):
    print(e.text)

for stu in root.iter('Student'):
    name = stu.find('Name')

    if name != None:
        name.set('text', name.text * 2)
        name.text = 'aaaaa'
        print(name.text)

stu = root.find('Student')
e = et.Element('ADDer')
e.attrib = {'a':'b'}
e.text = '�Ҽӵ�'

stu.append(e)

# һ��Ҫ���޸ĺ������д���ļ��������޸���Ч
tree.write('Student.xml')