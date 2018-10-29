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