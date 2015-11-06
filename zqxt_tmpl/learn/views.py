# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

import json
from django.shortcuts import render

def home(request):
    List = ['自强学堂','渲染Json到模板']
    Dict = {'site': '自强学堂','student':'LiuWenJu'}
    return render(request,'home.html',{
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    })
