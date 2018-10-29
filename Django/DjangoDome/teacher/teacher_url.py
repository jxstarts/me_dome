# coding=gbk
from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoDome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 视图函数名称只有名称，无括号和参数
    url(r'^tea/', views.do_app),

]
