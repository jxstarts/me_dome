# coding=gbk

from django.shortcuts import render
from django.http import HttpResponse
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