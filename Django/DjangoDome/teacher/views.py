# coding=gbk

from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse
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
# 5. URL�е�Ƕ�ײ���
def do_param2(r, pn):
    return HttpResponse("page number is {0}".format(pn))
# 6. ���ݶ������
def extemParam(r, name):
    return HttpResponse("My name is {0}".format(name))
# 7. URL�ķ������
def revParse(r):
    return HttpResponse("Your requested URL is {0}".format(reverse("askname")))