# �ṹ���ļ��洢
- xml��json
- Ϊ�˽����ͬ�豸֮����Ϣ����
- xml
- json
# xml�ļ�
- �ο�����
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html
    - https://blog.csdn.net/seetheworld518/article/details/49535285

- xml(eXtensibleMarkupLanguage) ����չ�������
    - ������ԣ�������ʹ�ü��������������ı��ַ������
    - ����չ���û������Զ�����Ҫ�ı��
    - ���磺
        <Teacher>
            �Զ�����Teacher
            ���������֮���κ����ݶ�Ӧ�ø�Teacher���
        </Teacher>  
    - ��w3c��ָ֯����һ����׼
    - XML�����������ݱ��������ݵĽṹ������
    - HTML�����������ʾwebҳ���е�����

- XML�ĵ��Ĺ���
    - ����ָ�������Ϊһ���ļ���ֻ��һ������ָ�
        - ���ֻ��һ��
        - �����ڵ�һ��
        - ��������XML���������ص�һЩ��������ָ��
        - ��xml�ؼ��ֿ�ͷ
        - һ������xml�İ汾�Ͳ��õı���
            - version����ʱ�����
            - encoding����������ָ��xml���������õı���
    - ��Ԫ�أ�һ���ļ���ֻ��һ����Ԫ�أ�
        - ������xml�ļ��У����԰�������һ�����νṹ
        - ��Ԫ������ֻ����һ��
    - ��Ԫ��
    - ����
    - ����
        - ������ǩ���洢����Ϣ
    - ע��
        - ��˵�����õ���Ϣ
        - ע�Ͳ���Ƕ���ڱ�ǩ��
        - ֻ����ע�͵Ŀ�ʼ�ͽ�β����˫�̺���
        - ���̺���ֻ�ܳ�����ע�͵Ŀ�ͷ���������ڽ�β
              
                <name> <!-- wangdapeng -->   </name> #����
                <name <!-- wangdapeng -->>   </name> #�����ԣ�ע���ڱ�ǩ��
                
                <!--my-name-by-wang--> #���ԣ�ע�����ݿ�����һ���̺���
                <!--my--name--by--wang-->#�����ԣ�˫�̺���ֻ�ܳ����ڿ�ͷ���β
                
                <!---my-name--> #���ԣ� ���̺���ֻ�ܳ����ڿ�ͷ
                <!---my-name---> #�����ԣ� ���̺���ֻ�ܳ����ڿ�ͷ        
        
- �����ַ��Ĵ���
    - xml��ʹ�õķ��ſ��ܸ�ʵ�ʷ������ͻ������͵ĵľ������Ҽ�����
    - ʹ��ʵ�����ã�ENtityReference������ʾ�����ַ�
        
             <score> score>80 </score> #�д���xml�в��ܳ���>
             <score> score&gt;80</score> #ʹ��ʵ������
    
    - �Ѻ��б����ַ��Ĳ��ַ���CDATA���ڲ���CDATA����ڲ���Ϣ��Ϊ����Ҫת��
        
             <![CDATA[
                select name,age
                from Student
                where score>80
              ]]>
    - ���õ���Ҫת��ı����ַ��Ͷ�Ӧʵ������
            - &:&amp;
            - <:&lt;
            - >:&gt;
            - ':&apos;
            - ":&quot;
            - һ������� ÿ��ʵ�����ö���&��ͷ�����ԷֺŽ�β
            
- xml��ǩ����������
    - Pascal������
    - �õ��ֱ�ʾ����һ����ĸ��д
    - ��Сд�ϸ�����
    - ��Ա�ǩ����һ��
- �����ռ�
    - Ϊ�˷�ֹ������ͻ
     <Student>
                        <Name>LiuYing</Name>
                        <Age>23</Age>
                </Student>
                <Room>
                    <Name>2014</Name>
                    <Location>1-23-1</Location>
                </Room>
                      
    - ����鲢��������������Ϣ���������ͻ
    
              <Schooler>
                        <Name>LiuYing</Name>
                        <Age>23</Age>
                    <Name>2014</Name>
                    <Location>1-23-1</Location>
                </Schooler>
                      
    - Ϊ�˱����ͻ����Ҫ�����ܳ�ͻԪ����������ռ�
    - xmlns: xml name space ����д
    
              <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
                        <student:Name>LiuYing</student:Name>
                        <Age>23</Age>
                        <romm:Name>2014</room:Name>
                        <Location>1-23-1</Location>
                </Schooler>
                
# xml����
   
## ��ȡ
- xml��ȡ��������Ҫ�ļ�����SAX��DOM
- SAX��Simple API for XML����
    - �����¼����� 
    - ����SAX�����ĵ���Ƶ����������¼�����������
    - �ص㣺
        - ��
        - ��ʽ��ȡ  
- DOM
    - ��W3C�涨��XML��̽ӿ�
    - һ��xml�ļ��ڻ����������νṹ���棬��ȡ
    - ��;��
        - ��λ���xml�κ�һ���ڵ���Ϣ
        - ���ɾ����Ӧ����
    - minidom
        - minidom.parse(filename):���ض�ȡ��xml�ļ�, filenameҲ������xml����
        - doc.documentElement:��ȡxml�ĵ�����һ��xml�ļ�ֻ��һ�����ڵ��ĵ�����
        - node.getAttribute(attr_name):��ȡxml�ڵ������ֵ
        - node.getElementByTagName(tage_name)���õ�һ���ڵ���󼯺�
        - node.childNodes:�õ����к��ӽڵ�
        - node.childNodes[index].nodeValue:��ȡ�����ڵ�ֵ
        - node.firstNode:�õ���һ���ڵ㣬�ȼ���node.childNodes[0]
        - node.attributes[tage_name]
        - ����v01
    - etree
        - �����νṹ����ʾxml
        - root.getiterator:�õ���Ӧ�Ŀɵ�����node����
        - root.iter
        - find(node_name):����ָ��node_name�Ľڵ�,����һ��node
        - root.findall(node_name):���ض��node_name�Ľڵ�
        - node.tag: node��Ӧ��tagename
        - node.text:node���ı�ֵ
        - node.attrib�� ��node�����Ե��ֵ����͵�����
        - ����v02
        
- xml�ļ�д��
    - ����
        - ele.set:�޸�����
        - ele.append: �����Ԫ��
        - ele.remove:ɾ��Ԫ��
        - ���� v03
    - ���ɴ���
        - SubElement, ����v04
        - minidom д�룬 ����v05
        - etree������ ����v06