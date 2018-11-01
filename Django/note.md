# �μ�����
    - https://github.com/tulingxueyuan

# Django
- ����
    - Python3.6
    - Django1.8
- �ο�����
    - [�ο�����]��https://yiyibooks.cn
    - Django��վ��16�ÿ�
# �����
- anaconda+pycharm
- anaconda��ʹ��
    - conda list����ʾ��ǰ������װ�İ�
    - conda env list����ʾ��װ�����⻷���б�
    - conda create -n env_name Python=3.6
    - ����conda�����⻷��
        - (Linux)source activate env_name
        - (win)conda activate env_name
    - pip install Django=1.8
    
# ��̨��Ҫ������


# ����һ��Django����
- �ҵ�������Ŀ�ļ����� Django-admin startproject DjangoDome
- ����Django
    - cd DjangoDome
    - anaconda prompt ������ Python manage.py runserver
- pycharm ����
    - ��Ҫ����
    
# ·��ϵͳ - urls
- ����APP
    - APP������һ������ҵ�����һ�����ҵ���ģ��
    - Python manage.py startapp env_name

- ·��
    - ���վ��������url�����뵽��Ӧ��ҵ����ģ���һ������
    - Django����Ϣ��������
    - �������ǽ��ܵ�URL����Ӧ�Ĵ���ģ���һ��ӳ��
    - �ڽ���URL�����ƥ����ʹ����RE
    - URL�ľ����ʽ��urls.py����ʾ

- ��Ҫ��ע���㣺
    1.���ܵ�URL��ʲô���������RE�Դ����URL����ƥ��
    2.��֪URLƥ�䵽�Ǹ�����ģ��
    
   
- urlƥ�����
    - ��������һ��һ���ȶ�
    - url��ʽ�Ƿּ���ʽ�����ռ���һ��һ�����±ȶ�,��Ҫ��Ӧurl������url�����
    - ��urlһ�������ã��򲻻᷵�ص���url
        - `/one/two/three/`
    - ������r��ͷ,��ʾ����Ҫת�壬ע����(^)����Ԫ����($)
        - `/one/two/three` ��� r'^one/
        - `/oo/one/two/three` ����� r'^one/"
        - `/one/two/three/` ��� r'three/$'
        - `/oo/one/two/three/oo/` ����� r'three/$"
        - ��ͷ����Ҫ�з�б��
    - ����������¶�û���ҵ����ʵ�ƥ�����ݣ��򱨴�
    
# 2. ����ӳ��
- ��ĳһ������RE��URLӳ�䵽���ﴦ������ȥ
    - ��������:
       '''
        from showeast import views as sv

        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap/', sv.normalmap),
        ]
       '''
# 3. URL�д�����ӳ��
- ���¼������������Ҫ��URL�������,���� /myurl/param�е�param
- ���������ַ�����ʽ,�����Ҫ��������ʽ��Ҫ����ת��
- ͨ������ʽ����:
    ```
      /search/page/432 �е� 432��Ҫ�����Ա任���������óɲ����ȽϺ���
    ```        ```
    
# 4. URL��app�д���
- �������Ӧ��URL������tulingxueyuan/urls.py��,���ܵ����ļ���ӷ��
- ���԰�urls���幦���𽥷�ɢ��ÿ��app��
    - ��django.conf.urls ���� include
    - ע���ʱRE���ֵ�д��
    - ���include����
- ʹ�÷���
    - ȷ��include������
    - д��·�ɵĿ�ͷurl
    - д��·��
    - ��дviews����
- ͬ������ʹ�ò���    

# 5. URL�е�Ƕ�ײ���
- ����ĳ��������һ����
- ����URL /index/page-3, ��Ҫ��������3��Ϊ����
    ```
    url(r'index_1/(page-(\d+)/)?$', sv.myindex_1), #��̫��
    url(r'index_2/(?:page-(?P<page_number>\d+)/)?$', sv.myindex_2), #��
    ```
- �������ӻ�õ���������,�� ?: �������Դ˲���    
    
# 6. ���ݶ������
- ����������������URL,�������������Լ����������
    ```
    url(r'extrem/$', sv.extremParam, {'name':"liuying"}),
    ```
- ���Ӳ���ͬ��������include���,��ʱ��include�����ж����


# 7. URL�ķ������
- ��ֹӲ����
- �������Ƕ�ÿһ��URL��������
- �Ժ��ٱ��������ʹ��URL��ֵ��ԭ���϶�Ӧ��ʹ�÷������

# views ��ͼ
# 1. ��ͼ����
- ��ͼ����ͼ����,����web���󲢷���web��Ӧ�����ﴦ����.
- ��Ӧָ����httpЭ��Ҫ����κ�����,����json,string, html��
- ���º���������,�ص�����η��ش�������
# 2 ��������ͼ
- django.http�������ṩ��ܶ��HttpResponse���Ƶļ���ͼ,
ͨ���鿴django.http��������֪��,
- ������ͼʹ�÷�����������,����ͨ��return�������ֱ�ӷ������ظ������
- Http404ΪException����,������Ҫraiseʹ��       

# 3. HttpResponse���
- ����
    - init ��ʹ��ҳ����ʵ����HttpResponse����
    - write(content)�����ļ��ķ�ʽд
    - flush()�����ļ��ķ�ʽ���������
    - set_cookie(key, value='', max_age=None, expires=None)������Cookie
       -  key,value�����ַ�������
       -  max_age��һ����������ʾ��ָ�����������
       -  expires��һ��datetime��timedelta���󣬻Ự�������ָ��������/ʱ����ڣ�ע��datetime��timedeltaֵֻ����ʹ��PickleSerializerʱ�ſ����л�
       -  max_age��expires��ѡһ
       -  �����ָ������ʱ�䣬���������ں����
    - delete_cookie(key)��ɾ��ָ����key��Cookie�����key��������ʲôҲ������

# 4. HttpResponseRedirect
   - �ض��򣬷���������ת
   - ���캯���ĵ�һ����������ָ���ض���ĵ�ַ
   - ���� ShowViews/views.py
            ```python
               # �� east/urls�����һ������
               url(r'^v10_1/', views.v10_1),
               url(r'^v10_2/', views.v10_2),
               url(r'^v11/', views.v11, name="v11"), 
            ```
            ```python
            # /east/ShowViews/views�����һ������
            def v10_1(request):
                return HttpResponseRedirect("/v11")
    
            def v10_2(request):
                return HttpResponseRedirect(reverse("v11"))
    
            def v11(request):
                return HttpResponse("����������v11�ķ��ʷ���ѽ")
    
            ```

# 5.Request����
- Request����
    - ���������յ�httpЭ�������󣬻���ݱ��Ĵ���HttpRequest����
    - ��ͼ�����ĵ�һ��������HttpRequest����
    - ��django.httpģ���ж�����HttpRequest�����API
- ����
    - ��������ر�˵�������Զ���ֻ����
    - path��һ���ַ�������ʾ�����ҳ�������·��������������
    - method��һ���ַ�������ʾ����ʹ�õ�HTTP����������ֵ������'GET'��'POST'
    - encoding��һ���ַ�������ʾ�ύ�����ݵı��뷽ʽ
        - ���ΪNone���ʾʹ���������Ĭ�����ã�һ��Ϊutf-8
        - ��������ǿ�д�ģ�����ͨ���޸������޸ķ��ʱ�����ʹ�õı��룬�����������Ե��κη��ʽ�ʹ���µ�encodingֵ
    - GET��һ���������ֵ�Ķ��󣬰���get����ʽ�����в���
    - POST��һ���������ֵ�Ķ��󣬰���post����ʽ�����в���
    - FILES��һ���������ֵ�Ķ��󣬰������е��ϴ��ļ�
    - COOKIES��һ����׼��Python�ֵ䣬�������е�cookie������ֵ��Ϊ�ַ���
    - session��һ���ȿɶ��ֿ�д���������ֵ�Ķ��󣬱�ʾ��ǰ�ĻỰ
        - ֻ�е�Django ���ûỰ��֧��ʱ�ſ��ã�
        - ��ϸ���ݼ���״̬���֡�
- ����
    - is_ajax()�����������ͨ��XMLHttpRequest����ģ��򷵻�True
    
- QueryDict����
    - ������django.http.QueryDict
    - request���������GET��POST����QueryDict���͵Ķ���
    - ��python�ֵ䲻ͬ��QueryDict���͵Ķ�����������ͬһ�������ж��ֵ�����
    - ����get()�����ݼ���ȡֵ
        - ֻ�ܻ�ȡ����һ��ֵ
        - ���һ����ͬʱӵ�ж��ֵ����ȡ���һ��ֵ
    - ����getlist()�����ݼ���ȡֵ
        - ������ֵ���б��أ����Ի�ȡһ�����Ķ��ֵ
- GET����
    - QueryDict���͵Ķ���
    - ����get����ʽ�����в���
    - ��url�����ַ�еĲ�����Ӧ��λ��?����
    - �����ĸ�ʽ�Ǽ�ֵ�ԣ���key1=value1
    - �������֮�䣬ʹ��&���ӣ���key1=value1&key2=value2
    - ���ǿ�����Ա�������ģ�ֵ�ǿɱ��
    - ����/views/v8_get

- POST����
    - QueryDict���͵Ķ���
    - ����post����ʽ�����в���
    - ��form���еĿؼ���Ӧ
    - ���пռ������name���ԣ�nameΪ����valueΪֵ
        - checkbox����һ����ֵ������
    - ���ǿ�����Ա�������ģ�ֵ�ǿɱ��
    - ����/views/v9_post
        - settings������ģ��λ��(�Ѿ��������)
        - ����getҳ���urls�ͺ���
                ```python
                    # east/urls.py
                    # ��Ҫ��·���ļ����������·��
                    url(r'^v9_get/', views.v9_get),
                    url(r'^v9_post/', views.v9_post),
                ```
                ```python
        
                     # ShowViews/views.py
                     # ���ļ��������������������
                    def v9_get(request):
                        return  render_to_response("for_post.html")
        
                    def v9_post(request):
                        rst = ""
                        for k,v in request.POST.items():
                            rst += k + "-->" + v
                            rst += ","
        
                        return HttpResponse("Get value of POST is {0} ".format(rst))
                ```
        - ����ļ�/east/templates/for_post.html
        - ���ڰ�ȫԭ����Ҫ�������а�ȫѡ����ɾ��csrf����
                ```python
                  # settings.py
                    MIDDLEWARE = [
                        'django.middleware.security.SecurityMiddleware',
                        'django.contrib.sessions.middleware.SessionMiddleware',
                        'django.middleware.common.CommonMiddleware',
                          #  ������仰��ע�͵�
                        #'django.middleware.csrf.CsrfViewMiddleware',
                        'django.contrib.auth.middleware.AuthenticationMiddleware',
                        'django.contrib.messages.middleware.MessageMiddleware',
                        'django.middleware.clickjacking.XFrameOptionsMiddleware',
                    ]
                ```
