# scrapy
# ������
- ���
- ������
    - scrapy
    - pyspider
    - crawley
- scrapy��ܽ���
    - https://doc.scrapy.org/en/latest/
    - http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html
- ��װ
    windows��װ�̳̣�https://www.cnblogs.com/xiaoli2018/p/4566639.html
    - ����pip
- scrapy ����
    - ������������
        - ScrapyEngine�������࣬���ԣ�����
        - Scheduler�����������淢����request���󣬵�������Ҫ����Ȼ�󽻻�����
        - Downloader�������������淢����requests�������󣬵õ�response
        - Spider���棺������������õ�����ҳ/������зֽ⣬�ֽ������+����
        - ItemPipeline�ܵ�����ϸ����Item
        - DownloaderMinddleware�����м�����Զ������صĹ�����չ���
        - SpiderMiddleware�����м������spider���й�����չ
- ������Ŀ�������
    - �½���Ŀ��scrapy startproject xxx
    - ��ȷ��ҪĿ��/��������дitem.py
    - �������棺��ַ spaider/xxspider.py
    - �洢���ݣ�pipelines.py

- ItenPipeline
    - ��Ӧ����pipelines�ļ�
    - ������ȡ�����ݴ���item��item�б����������Ҫ��һ����������������ȥ�أ��洢��
    - pipeline��Ҫ����process_item����
        - process_item��
            - spide��ȡ������item��Ϊ�������룬ͬʱ����Ļ���spider
            - �˷�������ʵ��
            - ���뷵��һ��Item���󣬱�������item���ᱻ֮���pipeline����
    - __init__�����캯��
        - ����һЩ��Ҫ�Ĳ�����ʼ��
    - open_spider(spider):
        - spider ���󱻿�����ʱ�����
    - close spider��spider��
        - ��spider�����¹رյ�ʱ�����

    - Spider
        - ��Ӧ�����ļ���spiders�µ��ļ�
        - __init__����ʼ���������ƣ�start_urls�б�
        - start requests������Requests���󽻸�Scprapy���ز�����response
        - parse�����ݷ��ص�response��������Ӧ��item��item�Զ�����pipeline�������Ҫ������url��url�Զ�����
        requestsģ�飬һֱѭ����ȥ
        - start request���˷������ܱ�����һ�Σ���ȡstart urls���ݲ�����ѭ������
        - name��������������
        - start_urls�����ÿ�ʼ��һ����ȡ��url
        - allow domains��spider ������ȡ�������б�
        - stastart_request(self)��ֻ������һ��
        - parse
        - log����־��¼
    - �м����DowloaderMiddlewares��
        - �м���ǳ���������������м��һ�����
        - �����кܶ��������˳�����ִ��
        - �����ǶԷ���������ͷ��صĽ������Ԥ����
        - ��middlewares�ļ���
        - ��Ҫ��settings�������Ա���Ч
        - ��д�м��ʮ�ּ򵥣��м��������scrapy.contrib.dowliadermiddleware.DownloaderMiddleware������
        - һ��һ���м�����һ���
        - ����ʵ������һ�����߶������
            - process_request(self, request, spider)
                - ��requestͨ����ʱ�򱻵���
                - ���뷵��None��Response��Request��raise IgnoreRequest
                - None: scrapy�����������request
                - Request�� scrapy��ֹͣ����process_request����ϴ���ȷ��ص�reqeust
                - Response�� scrapy�������������process_request����process_exception��ֱ�ӽ���response��Ϊ�������
                ͬʱ�����process_response����
            - process_response(self, request, response,  spider)
                - ��process_request��ͬС��
                - ÿ�η��ؽ����ʱ����Զ�����
                - �����ж������˳�����
        - ��������

                import random
                import base64

                # ��settings�����ļ��е���ֵ
                from settings import USER_AGENTS
                from settings import PROXIES

                #  ����� User-Agent
                class RandomUserAgent(object):
                    def process_request(self, request, spider):
                        useragent = random.choice(USER_AGENTS)
                        request.headers.setdefault("User-Agent", useragent)

                class RandomProxy(object):
                    def process_request(self, request, spider):
                        proxy = random.choice(PROXIES)
                        if proxy['user_passwd'] is None:
                            #  û�д����˻���֤�Ĵ���ʹ�÷�ʽ
                            request.meta['proxy'] = "http://" + proxy['ip_port']
                        else:
                            #  ���˻�������� base64 ����ת��
                            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
                            #  ��Ӧ������������������ʽ��
                            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd
                            request.meta['proxy'] = "http://" + proxy['ip_port']
        - ����settings����ش���


                USER_AGENTS = [
                            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR
                            3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0;
                            SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET
                            CLR 1.1.4322)",
                            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR
                            2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko,
                            Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)
                            Arora/0.6",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-
                            Ninja/2.1.1",
                            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0
                            Kapiko/3.0",
                            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
                            ]

                PROXIES = [
                        {'ip_port': '111.8.60.9:8123', 'user_passwd': 'user1:pass1'},
                        {'ip_port': '101.71.27.120:80', 'user_passwd': 'user2:pass2'},
                        {'ip_port': '122.96.59.104:80', 'user_passwd': 'user3:pass3'},
                        {'ip_port': '122.224.249.122:8088', 'user_passwd': 'user4:pass4'},
                        ]
- ȥ��
    - Ϊ�˷�������������ѭ������Ҫȥ��
    - ����spider�е�parse�����У�����Request��ʱ�����dont_filter=False����

            myspeder(scrapy.Spider):
                def parse(.....):

                    ......

                    yield  scrapy.Request(url=url, callback=self.parse, dont_filter=False)

- �����scrapyʹ��selenium
    - ���Է����м���е�process_request������
    - �ں����е���selenium�������ȡ�󷵻�Response


            calss MyMiddleWare(object):
                def process_request(.....):

                    driver = webdriver.Chrome()
                    html = driver.page_source
                    driver.quit()

                    return HtmlResponse(url=request.url, encoding='utf-8', body=html, request=request)


����e16-qq��Ƹ
    - ������Ŀ
    - ��дitem
    - ��дspider
    - ��дpipeline
    - ����pipeline

- ���� e14-scrapy-baidu
    - ������򵥵�����
    - ��ȥ�ٶ�ҳ��
    - �ر����û�����Э��
    - scrapy startproject baidu
    - scrapy crawl baidu

- ����e15-meiju
    - ��������Ŀ
    - ������ҳ������item
    - ��дpipeline�� ȷ����δ���item
    - ��дspider�� ȷ�������ȡitem
    - ����ͨ������һ�����������ļ��ķ�ʽ��pycharm����������

- ����e17-У����
    - ������Ŀ
    - ��дitem
    - spider
    - pipeline
    - ����pipeline
    - �м���� ��ʹ��selenium