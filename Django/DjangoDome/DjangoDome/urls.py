from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv
from teacher import teacher_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoDome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # ��ͼ��������ֻ�����ƣ������źͲ���
    url(r'^normalmap/', tv.do_normalmap),

    # Լ�����������ó�����ģ�鴦�����ͼ��url����teacher��ͷ
    url(r'^teacher/', include(teacher_url)),

    # ����������ͼ����
    # ��ű�ʾ�Ժ������ݿ�ͷ�ı��ʽ
    # Բ���ű�ʾ����һ�������������������Ϊ�������ݸ������õĺ���
    # �����������ʺüӴ�дP��ͷ��������������ǲ���������
    # �����ź��ʾ����[0-9]��ʾ���ݽ�������0-9�����ֹ��ɣ�
    # ��������ű�ʾ���ֵĴ������˴�4��ʾֻ�ܳ����ĸ�0-9������
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),  # ����ӳ��

]
