# coding=gbk
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoDome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # ��ͼ��������ֻ�����ƣ������źͲ���
    url(r'^tea/', views.do_app),

]
