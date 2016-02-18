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

def home(request):
    t = get_template('index.html')
    return HttpResponse(t.render())

def get_rand_img(request):
    tab_id = request.GET.get('tab_id')
    tabn = sum([int(i) for i in tab_id.split('-')[1:]])
    fname = str((int(random.random() * 100) + tabn) % 5 + 1) + '.jpg'
    return JsonResponse({'img_link': '/static/' + fname})