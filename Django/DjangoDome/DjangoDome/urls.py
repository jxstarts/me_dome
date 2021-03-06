
# coding=gbk
from django.conf.urls import include, url
from django.contrib import admin

from teacher import views as tv
from teacher import teacher_url

urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoDome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 视图函数名称只有名称，无括号和参数
    url(r'^normalmap/', tv.do_normalmap),

    # 带参数的视图函数
    # 尖号表示以后面内容开头的表达式
    # 圆括号表示的是一个参数，里面的内容作为参数传递给被调用的函数
    # 参数名称以问好加大写P开头，尖括号里面就是参数的名字
    # 尖括号后表示正则，[0-9]表示内容仅能是有0-9的数字构成，
    # 后面大括号表示出现的次数，此处4表示只能出现四个0-9的数字
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', tv.withparam),  # 正常映射

    # 约定凡是由特拿出个人模块处理的视图的url都以teacher开头
    url(r'^teacher/', include(teacher_url)),
    # 5. URL中的嵌套参数
    url(r'^book/(?:page-(?P<pn>\d+))$', tv.do_param2),
    # 6. 传递额外参数
    url(r'^yourname/$', tv.extemParam, {"name":"hahaha"}),
    # 7. URL的反向解析
    url(r'^yourname1/$', tv.revParse, name="askname")
]
