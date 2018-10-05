import xml.etree.ElementTree as et

stu = et.Element("Student3")

name = et.SubElement(stu, 'Name')
name.attrib = {'lang', 'en'}
name.text = 'hahaha'

age = et.SubElement(stu, 'Age')
age.text = 18

et.dump(stu)