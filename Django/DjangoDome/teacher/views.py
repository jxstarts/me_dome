# coding=gbk

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
��ͼ������Ҫһ������������Ӧ���� HTTPRequest
'''

def do_normalmap(request):
    return HttpResponse("���� normalmap")

# ����������ͼ����
def withparam(request,year, month):
    return HttpResponse("This is with param {0}, {1}".format(year, month))

def do_app(r):
    return HttpResponse("�������·��")