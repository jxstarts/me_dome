# ҳ�������������ȡ
- �ṹ���ݣ����нṹ����̸����
    - JSON�ļ�
        - JSON Path
        - ת����Python���ͽ��в�����json�ࣩ
    - XML�ļ�
        - ת����Python���ͣ�xmltodict��
        - XPath
        - CSSѡ����
        - ����
- �ǽṹ�����ݣ��������ݣ���̸�ṹ
    - �ı�
    - �绰����
    - �����ַ
        - ͨ������������ݣ�ʹ��������ʽ
    - HTML�ļ�
        - ����
        - XPath
        - CSSѡ����
        
# ������ʽ
- һ�׹��򣬿������ַ����ı��н����Ѳ��滻��
- ����v23,re�Ļ���ʹ������
- ����v24��match�Ļ���ʹ��
    - match: �ӿ�ʼλ�ÿ�ʼ���ң�һ��ƥ��
    - search�����κ�λ�ò��ң�һ��ƥ�� ����v25
    - finfall:ȫ��ƥ�䣬�����б� ����v26
    - finditer��ȫ��ƥ�䣬�����б� ����v26
    - split: �ָ��ַ����������б�
    - sub���滻

- ƥ������
    - ����Unicode��Χ��Ҫ��[u4e00 - u9fa5]
    - ����v27

- ̰�����̰��
    - ̰��ģʽ�����������ʽ��ƥ��ɹ���ǰ���£������ܶ��ƥ��
    - ��̰��ģʽ�����������ʽ��ƥ��ɹ���ǰ���£��������ٵ�ƥ��
    - Python����������Ĭ����̰��ģʽ
    - ���磺
        - �����ı�abbbbbbbbccccc
        - re ��ab*
        - ̰��ģʽ�������abbbbbbbb
        - ��̰��ģʽ�������a

# XML
- XML(EXtensibleMarkupLanguage)
- http://w3school.com.cn/xml/index.asp
- ����v28
- ������ڵ㣬�ӽڵ㣬�ȱ��ڵ㣬�ֵܽڵ㣬����ڵ�

# XPath
- XPath��XML Path Language������һ����XML�ĵ��в�����Ϣ������
- �ٷ��ĵ���http://www.w3school.com.cn/xpath/index.asp
- XPath��������
    - ��Դ��XPath���ʽ���ߣ�XMLQuire
    - Chrome�����XPath Helper
    - Firefox�����XPath CHecker

- ����·�����ʽ
    - nodename��ѡȡ�ڵ����е��ӽڵ�
    - /: �Ӹ��ڵ㿪ʼѡ
    - //: ��ȡԪ�����ݣ���������Ԫ�صľ���λ��
    - .: ��ǰ�ڵ�
    - ..: ���ڵ�
    - @�� ѡȡ����
    - ������
        - bookstore��ѡȡbookstore�µ����н���
        - /bookstore��ѡȡ��Ԫ��
        - bookstore/book��ѡȡbookstore������Ϊbook��Ԫ��
        - //book��ѡȡbook��Ԫ��
        - //@lang:ѡȡ����Ϊlang����������
- ν�Predicates��
    - ν����������ĳ���ض��Ľڵ㣬����Ƕ�ڷ�������
    - /bookstore/book[1]��ѡȡ����bookstore�½�book��Ԫ��
    - /bookstore/book][last()]: ѡȡ���һ������bookstore�½�book��Ԫ��
    - /bookstore/book[last()-1]: ѡȡ�����ڶ�������bookstore�½�book��Ԫ��
    - /bookstore/book[last()<3]: ѡȡ������bookstore�½�book��ǰ����Ԫ��
    - /bookstore/book[@lang]:ѡȡ������bookstore�½�book�ĺ�������lang��Ԫ��
    - /bookstore/book[@lang="cn"]:ѡȡ������bookstore�½�book�� ��������lang��ֵ��cn��Ԫ��
    - /bookstore/book[@price < 90]:ѡȡ������bookstore�½�book�� ����price�ģ���ֵС��90��Ԫ��
    - /bookstore/book[@price < 90]:ѡȡ������bookstore�½�book�� ����price�ģ���ֵС��90��Ԫ�ص���Ԫ��title

- ͨ���
    - '*'���κ�Ԫ�ؽڵ�
    - @*��ƥ���κ����Խڵ�
    - node()��ƥ���κ����͵Ľڵ�
- ѡȡ���·��
    - //book/title  |  //book/author:ѡȡbookԪ���е�title��authorԪ��
    - //title | //price��ѡȡ�ĵ������е�title��priceԪ��

# lxml��
- Python��HTML/XML�Ľ�����
- �ٷ��ĵ��� http://lxml.de/index.html
- ����v29
- ���ܣ�
    - ����HTML
    - �ļ���ȡ������v30��v31
    - etree��XPath�����ʹ�ã�����v32
    
# CSSѡ���� BeautifulSoup4
- ����ʹ��BeautifulSoup4
- http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
- ����������ȡ��Ϣ���ߵıȽϣ�
    - ���򣺺ܿ죬�����ã����ð�װ
    - beautifulsoup������ʹ�ü򵥣���װ��
    - lxml���ȽϿ죬ʹ�ü򵥣���װһ��
- ����v33
- �Ĵ����
    - Tag
        - ��ӦHTML�еı�ǩ
        - ����ͨ��soup.tag_name
        - tag������Ҫ����
            - name
            - attrs
        - ����v34
    - NavigableString
        - ��Ӧ����ֵ
    - BeautifulSoup
        - ��ʾ����һ���ĵ������ݣ��󲿷ֿ��԰�������tag����
        - һ�����ǿ�����soup��ʾ
    - Comment
        - �������͵�NavigableString����
        - ��������������ݲ�����ע�ͷ���
        
- �����ĵ�����
    - contents��tag���ӽڵ����б�ķ�ʽ����
    - children���ӽڵ��Ե�������ʽ����
    - descendants:�����ӽڵ�
    - String
    - ����v34
- �����ĵ�����
    - find_all(name, attrs, recursive, text, **kwargs)
        - name�������ĸ��ַ������������Դ��������Ϊ
            - �ַ���
            - ������ʽ
            - �б�
        - kewwortd����������������ʾ����
        - text����Ӧtag���ı�ֵ
        - ����v34
        

    