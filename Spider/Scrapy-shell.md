# scrapy - shell
- http://segmentfault.com/a/1190000013199636?utm_source=tag-newest
- shell
- ����
    - Linux��ctr+T,���ն�Ȼ������scrapy shell"url:xxx"
    - Windows��scrapy shell "url:xxx"
    - �������Զ�����ָ����url����ҳ
    - ������ɺ�url�����ݱ�����response�ı����У������Ҫ��������Ҫ����response
        - ��ȡ�������ݱ�����response�и�
        - response.body����ҳ�Ĵ���
        - response.headers�Ƿ��ص�http��ͷ��Ϣ
        - response.xpath����ʹ��xpath�﷨ѡ������
        - response.css()����ʹ��css�﷨ѡȡ����
    - selector
        - ѡ�����������û�ʹ��ѡ������ѡ���Լ���Ҫ������
        - response.selector.xpath��response.xpath��select.xpath�Ŀ�ݷ�ʽ
        - response.selector.css:response.css�����ǵĿ�ݷ�ʽ
        - selector.extract���ѽڵ��������unicode��ʽ����
        - selector.re�������û�ͨ������ѡȡ����
    