# -*- coding: utf-8 -*-
__author__ = 'Adward'

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
from django.core.files import File
import os
from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.utils import json
from django.http import JsonResponse
import random
import json
import sqlite3
from js_ex_01.models import WeiboData

def home(request):
    t = get_template('index.html')
    return HttpResponse(t.render())

def insertData(request): #called once
    XRANGE = 24
    print(os.listdir(os.path.dirname(__file__)))
    path = os.path.join(os.path.dirname(__file__), 'weibo.json')
    with open(path) as f:
        data = json.load(f)
    print(data['children'][0])
    for dataset in data['children']:
        set_idx = dataset['name']
        for i in range(XRANGE):
            row = dataset['children'][i]
            record = WeiboData(index=set_idx*XRANGE+i,
                               level1=row['level0'],
                               level2=row['level1'],
                               level3=row['level2'])
            record.save()
    return HttpResponse()

def get_chart_data(request):
    XRANGE = 24
    tab_id = request.GET.get('tab_id')
    tabn = 0
    for i in tab_id.split('-')[1:]:
        tabn = tabn * 10 + int(i)
    set_idx = int(random.random() * 10 * tabn) % 100
    #set_idx = 5
    chart_data = []
    for i in range(set_idx*XRANGE, (set_idx+1)*XRANGE):
        obj = WeiboData.objects.get(index=i)
        chart_data.append([obj.level1, obj.level2, obj.level3])
    return JsonResponse({'cdata': chart_data})