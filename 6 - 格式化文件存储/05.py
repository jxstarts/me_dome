import xml.dom.minidom

# ���ڴ��д���һ���յ��ĵ�
doc = xml.dom.minidom.Document()
# ����һ�����ڵ�Managers����
root = doc.createElement('Managers')
# ���ø��ڵ������
root.setAttribute('company', 'xx�Ƽ�')
root.setAttribute('address', '�Ƽ����԰')
# �����ڵ���ӵ��ĵ�������
doc.appendChild(root)

managerList = [{'name' : 'joy',  'age' : 27, 'sex' : 'Ů'},
               {'name' : 'tom', 'age' : 30, 'sex' : '��'},
               {'name' : 'ruby', 'age' : 29, 'sex' : 'Ů'}
]

for i in managerList :
  nodeManager = doc.createElement('Manager')
  nodeName = doc.createElement('name')
  # ��Ҷ�ӽڵ�name����һ���ı��ڵ㣬������ʾ�ı�����
  nodeName.appendChild(doc.createTextNode(str(i['name'])))

  nodeAge = doc.createElement("age")
  nodeAge.appendChild(doc.createTextNode(str(i["age"])))

  nodeSex = doc.createElement("sex")
  nodeSex.appendChild(doc.createTextNode(str(i["sex"])))

  # ����Ҷ�ӽڵ���ӵ����ڵ�Manager�У�
  # ���Manager��ӵ����ڵ�Managers��
  nodeManager.appendChild(nodeName)
  nodeManager.appendChild(nodeAge)
  nodeManager.appendChild(nodeSex)
  root.appendChild(nodeManager)
# ��ʼдxml�ĵ�
fp = open('Manager.xml', 'w')
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")