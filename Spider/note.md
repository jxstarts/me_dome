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
        - Ϊ�˸��������������Ϣ��������ͨ��urlopen�����Ѿ���̫������
        - ��Ҫ����request.Request��
        - ����v06
        
- yrllib.error
    - URLError������ԭ��
        - ����
        - ����������ʧ��
        - �Ҳ���ָ��������
        - ��OSError������
        - ����v07
    - HTTPError,��URLError��һ������
        - ����v08
        
    - ��������
        - HTTPError�Ƕ�Ӧ��HTTP����ķ��������������ش�������400���ϵģ�����������HTTPError
        - URLError��Ӧ��һ��������������⣬����url����
        - ��ϵ����OSError - URLError - HTTPError   
- UserAgent
    - UserAgent���û������״��ƺ�UA������heads��һ���֣�������ͨ��UA���жϷ��������
    - ������UAֵ��ʹ�õ�ʱ�����ֱ�Ӹ���ճ����Ҳ��������������ʵ�ʱ��ץ��
        
            1.Android

            Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19
            Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30
            Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

            2.Firefox

            Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0
            Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0

            3.Google Chrome

            Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36
            Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19

            4.iOS

            Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3
            Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3
    
    - ����UA����ͨ�����ַ�ʽ��
        - heads
        - add_header
        - ����v09
        
        
- ProxyHandler���������������
    - ʹ�ô���IP�������泣�õ��ֶ�
    - ��ȡ����������ĵ�ַ��
        - www.xicidaili.com
        - www.goubanjia.com
    - ��������������ʵ�����У�����Ҳ������Ƶ������ĳһ���̶���վ�����ԣ�����һ��Ҫ�ܶ�ܶ�
    - ����ʹ�ò��裺
        1.���ô����ַ
        2.����ProxyHandler
        3.����Opener
        4.��װOpener
    - ����v10

- cookie & session
    - ����http���޼����ԣ�����Ϊ���ֲ����ȱ���������õ�һ������Э��
    - cookie�Ƿ����û�����http���������һ����Ϣ��session�Ǳ����ڷ������ϵĶ�Ӧ��һ����Ϣ��������¼�û���Ϣ

- cookie��session������
    - ���λ�ò�ͬ
    - cookie����ȫ
    - session�ᱣ���ڷ�������һ��ʱ��
    - ����cookie�������ݲ�����4k���ܶ����������һ��վ����ౣ��20��
- session�Ĵ��λ��
    - ���ڷ�������
    - һ�������session�Ƿ����ڴ��л������ݿ���
    - û��cookie��¼ ����v11�����Կ�����û��ʹ��cookie������ҳΪδ��¼״̬
    
- ʹ��cookie��¼
    - ֱ�Ӱ�cookie����������Ȼ���ֶ���������ͷ������v12
    - httpģ�鲻�ú�һЩ����cookie��ģ�飬ͨ���������ǿ����Զ�ʹ��cookie
        - CookieJar
            - ����洢cookie���򴫳���http�������cookie��
            - cookie�洢���ڴ��У�CookieJarʵ�����պ�Cookie��Сʱ
        - FileCookieJar��filename��delayload=None��policy=None����
            - ʹ���ļ�����cookie
            - filename�Ǳ���cookie���ļ�
        - MozillaCookieJar��filename��delayload=None��policy=None����
            - ������mocilla�����cookie.txt���ݵ�FileCookieJarʵ��
        - LwpCookieJar��filename��delayload=None��policy=None����
            - ������libwww-perl��׼��Set-Cookie3��ʽ��FileCookieJarʵ��
        - ���ǵĹ�ϵ�ǣ�CookieJar --> FileCookieJar -->MozillaCookieJar & LwpCookieJar
    - ����CookieJar�������ˣ�����v13
        - �Զ�ʹ��cookie��¼������������
        - �򿪵�¼ҳ����Զ�ͨ���û��������¼
        - �Զ���ȡ����������cookie
        - ������ȡ��cookie��¼��˽ҳ��
    - handler �� handler��ʵ�������òο���������
            # ���� cookie�Ĺ�����
            cookie_handler = request.HTTPCookieProcessor(cookie)
    
            # ����http���������
            http_handler = request.HTTPHandler()
            
            # ����HTTPS������
            https_handler = request.HTTPSHandler()
    - ����handler��ʹ��opener�򿪣��򿪺���Ӧ��ҵ������Ӧ��handler����
    - cookie��Ϊһ����������ӡ����������v14
        - name: ����
        - value��ֵ
        - domain�����Է��ʴ�cookie������
        - path�� ���Է��ʴ�cookie��ҳ��·��
        - expires������ʱ��
        - size����С
        - HTTP�ֶ�
    - cookie �ı��� - FileCookieJar������v15
    - cookeie �Ķ�ȡ�� ����v16
    
- SSL
    - SSL֤�����ָ����SSL��ȫ�׽ײ�Э��ķ���������֤�飨SercureSocketLayer��
    - ����������˾����
    - CA��CertifacateAuthority��������֤����֤���ģ��Ƿ��ţ������ϳ�����֤��������˵ĵ���������
    - ���������ε�SSL֤�飬��Ҫ������������v17
    
- js ����
 - �еķ�������Բ���js����Ҫ��������ݽ��м��ܴ���ͨ����md5ֵ��
 - �������ܣ�����ľ������ģ�����
 - ���ܺ������߹���һ�������������ɣ�Ҳ����һ����Ѵ��루js���룩��¶��ʹ����
 - ͨ���Ķ������㷨���Ϳ���ģ������ܹ��̣��Ӷ��ﵽ�ƽ�
 - ���̲ο�����v18
    
            
