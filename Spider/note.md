# 0 ����׼������
- �ο�����
    - Python �������ݲɼ��� ͼ�鹤ҵ����
    - ��ͨPython������Scrapy�������ʵ������
    - [Python3��������](http://blog.csdn.net/c406495762/article/details/72858983)
    - [Scrapy�ٷ��̳�](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
- ǰ��֪ʶ
    - url
    - httpЭ��
    - webǰ�ˡ�HTML�� css��js
    - ajax
    - re��xpath
    - xml

# 1.������
- ���涨�壺�������棨�ֱ���Ϊ��ҳ֩�롤��������ˣ���FOAF�����м䣬�������ĳ�Ϊ��ҳ׷���ߣ���
��һ�ְ���һ���Ĺ����Զ���ץȡ��ά����Ϣ�ĳ�����߽ű���
����һЩ����ʹ�õ����ֻ������ϡ��Զ�������ģ�����������
- ��������
    - �ܰ�����Ҫ���������ݻ�������
    - ���Զ�������������
- �����裺
    - ������Ϣ
    - ��ȡ��ȷ����Ϣ
    - ����һ�������Զ������������ҳ��ִ����������
- �������
    - ͨ������
    - ר�����棨�۽����棩
- Python��������
    - Python2.x��urllib, urllib2, urllib3, httplib, httplib2, requests
    - Python3.x: urllib, urllib3, httplib2, requests
    - python2: urllib��urllib2���ʹ�ã�����requests
    - Python3�� urllib��requests
# 2. urllib
- ����ģ��
    - urllib.request:�򿪺Ͷ�ȡurls
    - urllib.error:����urllib.request�����ĳ����Ĵ���ʹ��try��׽
    - urllib.parse����������url�ķ���
    - urllib.robotparse:����robots.txt�ļ�
    - ����v01

- ��ҳ�ı�������Ľ��
    - chardet �����Զ����ҳ���ļ��ı����ʽ�����ǣ���������
    - ��Ҫ��װ��conda install chardet
    - ����v02
- urlopen �ķ��ض���
    - ����v03
    - geturl:������������url
    - info�������������meta����Ϣ
    - getcode�����ص�http code
- request.date ��ʹ��
    - ������������ַ���
    - get��
        - ���ò�����������������Ϣ
        - ����Ϊdict��Ȼ����parse����
        - ����v04
    - post
        - һ������������ݲ���ʹ��
        - post�ǰ���Ϣ�Զ����ܴ���
        - ���������ʹ��post��Ϣ����Ҫ�õ�data����
        - ʹ��post����ζ��http������ͷ������Ҫ���ģ�
            - Content-Type��application/x-www.from-urlencode
            - Content-Length�����ݳ���
            - �����֮һ���������󷽷�����ע����������ͷ����Ϣ����Ӧ
        - urllib.parse.urlencode���Խ��ַ����Զ�ת���������
        - ����v05   
