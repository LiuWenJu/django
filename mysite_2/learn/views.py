#coding=utf-8
#from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse(u"Welcome Django! Fuck gfw!   这是我的第一个Django 项目")

# Create your views here.
