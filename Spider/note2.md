# ҳ�������������ȡ
- �ṹ���ݣ� ���еĽṹ����̸����
    - JSON�ļ�
        - JSON Path
        - ת����Python���ͽ��в�����json�ࣩ
    - XML�ļ�
        - ת����python���ͣ�xmltodict��
        - XPath
        - CSSѡ����
        - ����
- �ǽṹ�����ݣ��������ݣ���̸�ṹ
    - �ı�
    - �绰����
    - �����ַ
        - ͨ������������ݣ�ʹ��������ʽ
    - Html�ļ�
        - ����
        - XPath
        - CSSѡ����
       
# ������ʽ
- һ�׹��򣬿������ַ����ı��н����Ѳ��滻��
- ����v23,re�Ļ���ʹ������
- ����v24��match�Ļ���ʹ��
- �����÷�����
    - match: �ӿ�ʼλ�ÿ�ʼ���ң�һ��ƥ��
    - search�����κ�λ�ò��ң�һ��ƥ�䣬 ����v25
    - findall�� ȫ��ƥ�䣬�����б�, ����v26
    - finditer�� ȫ��ƥ�䣬���ص�����, ����v26
    - split�� �ָ��ַ����������б�
    - sub���滻
- ƥ������
    - ����unicode��Χ��Ҫ��[u4e00-u9fa5]
    - ����v27
    
- ̰�����̰��ģʽ
    - ̰��ģʽ�� ���������ʽƥ��ɹ���ǰ���£������ܶ��ƥ��
    - ��̰��ģʽ�� xxxxxxxxxxxxxxxxxxxxxx, �������ٵ�ƥ��
    - python����������Ĭ����̰��ģʽ
    - ���磺
        - �����ı�abbbbbbccc
        - re�� ab*
        - ̰��ģʽ�� �����abbbbbb
        - ��̰���� �����a
# XML
- XML(EXtensibleMarkupLanguage)   
-    http://www.w3school.com.cn/xml/index.asp
- ����v28.xml
- ������ڵ㣬�ӽڵ㣬�ȱ��ڵ㣬�ֵܽڵ㣬����ڵ�

# XPath
- XPath(XML Path Language), ��һ����XML�ĵ��в�����Ϣ�����ԣ�
- �ٷ��ĵ��� http://www.w3school.com.cn/xpath/index.asp
- XPath��������
    - ��Ԫ��XPath���ʽ���ߣ� XMLQuire
    - chrome����� Xpath Helper
    - Firefox����� XPath CHecker
    
- ����·�����ʽ��
    - nodename: ѡȡ�˽ڵ�������ӽڵ�
    - /: �Ӹ��ڵ㿪ʼѡ
    - //: ѡȡԪ�أ���������Ԫ�صľ���Ϊֹ
    - .:  ��ǰ�ڵ�
    - ..:���ڵ�
    - @�� ѡȡ����
    - ������
        - booksotre: ѡȡbookstore�µ������ӽڵ�
        - /booksotre: ѡȡ��Ԫ��
        - booksotre/book: ѡȡbookstore������Ϊbook����Ԫ��
        - //book: ѡȡbook��Ԫ��
        - //@lang:ѡȡ����Ϊlang����������
- ν��(Predicates)
    - ν����������ĳ���ض��Ľڵ㣬����ǰ�ڷ�������
    - /bookstore/book[1]: ѡȡ��һ������bookstore�½�book��Ԫ��
    - /bookstore/book[last()]: ѡȡ���һ������bookstore�½�book��Ԫ��
    - /bookstore/book[last()-1]: ѡȡ�����ڶ�������bookstore�½�book��Ԫ��
    - /bookstore/book[position()<3]: ѡȡ����bookstore�½�book��ǰ����Ԫ��
    - /bookstore/book[@lang]: ѡȡ����bookstore�½�book��,��������langԪ��
    - /bookstore/book[@lang="cn"]: ѡȡ����bookstore�½�book��,��������lang��ֵ��cn��Ԫ��
    - /bookstore/book[@price < 90]: ѡȡ����bookstore�½�book��,��������price�ģ���ֵС��90��Ԫ��
    - /bookstore/book[@price < 90]/title: ѡȡ����bookstore�½�book��,��������price�ģ���ֵС��90��Ԫ�ص���Ԫ��title
    
- ͨ���
    - `*` : �κ�Ԫ�ؽڵ�
    - @*�� ƥ���κ����Խڵ�
    - node(): �����κ����͵Ľڵ�
- ѡȡ���·��
    - //book/tile  | //book/author : ѡȡbookԪ���е�title��authorԪ��
    - //tile | //price: ѡȡ�ĵ������е�title��priceԪ��
  
# lxml��
- python��HTML/XML�Ľ�����
- �ٷ��ĵ���   http://lxml.de/index.html
- ���ܣ�
    - ����HTML,����v29.py
    - �ļ���ȡ������v30.html, v31.py
    - etree��XPath�����ʹ��, ����v32.py

# CSSѡ����  BeautifulSoup4
- ����ʹ��BeautifulSoup4
- http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
- ����������ȡ��Ϣ���ߵıȽϣ�
    - ���� �ܿ죬�����ã�����װ
    - beautifulsoup������ʹ�ü򵥣���װ��
    - lxml�� �ȽϿ죬ʹ�ü򵥣���װһ��
- ����v33.py
- �Ĵ����
    - Tag
    - NavigableString
    - BeautifulSoup
    - Comment
- Tag
    - ��ӦHtml�еı�ǩ
    - ����ͨ��soup.tag_name
    - tag������Ҫ����
        - name
        - attrs
    - ����a34  
 
- NavigableString
    - ��Ӧ����ֵ
  
- BeautifulSoup
    - ��ʾ����һ���ĵ������ݣ��󲿷ֿ��԰�������tag����
    - һ�����ǿ�����soup����ʾ
- Comment
    - �������͵�NavagableString���� 
    - ��������������ݲ�����ע�ͷ���
- �����ĵ�����
    - contents: tag���ӽڵ����б�ķ�ʽ���� 
    - children�� �ӽڵ��Ե�������ʽ���� 
    - descendants�� ������ڵ�
    - string
    - ����34
- �����ĵ�����
    - find_all(name, attrs, recursive, text, ** kwargs)  
        - name:�����Ǹ��ַ������������Դ��������Ϊ
            - �ַ���
            - ������ʽ
            - �б�
        - kewwortd����������������ʾ����
        - text�� ��Ӧtag���ı�ֵ
        - ����34
            
- cssѡ����
    - ʹ��soup.select, ����һ���б�
    - ͨ����ǩ����: soup.select("title")            
    - ͨ�������� soup.select(".content")
    - id����: soup.select("#name_id")
    - ��ϲ���: soup.select("div #input_content")
    - ���Բ���: soup.select("img[class='photo'])
    - ��ȡtag���ݣ� tag.get_text
    - ����35