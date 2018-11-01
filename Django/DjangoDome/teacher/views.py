# coding=gbk

from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse
# Create your views here.

'''
视图函数需要一个参数，类型应该是 HTTPRequest
'''

def do_normalmap(request):
    return HttpResponse("这是 normalmap")

# 带参数的视图函数
def withparam(request,year, month):
    return HttpResponse("This is with param {0}, {1}".format(year, month))

def do_app(r):
    return HttpResponse("这个是子路由")
# 5. URL中的嵌套参数
def do_param2(r, pn):
    return HttpResponse("page number is {0}".format(pn))
# 6. 传递额外参数
def extemParam(r, name):
    return HttpResponse("My name is {0}".format(name))
# 7. URL的反向解析
def revParse(r):
    return HttpResponse("Your requested URL is {0}".format(reverse("askname")))