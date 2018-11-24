# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bad_request(request):
    return render(request, '400.html')

def permission_denied(request):
    return render(request, '403.html')

def page_not_found(request):
    return render(request, '404.html')

def page_error(request):
    return render(request, '500.html')

