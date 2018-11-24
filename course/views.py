# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse,FileResponse
import csv

# Create your views here.

def index(request, year):
    if year == "2000":
        #return HttpResponse('hello %s' % year)

        #return HttpResponse('hello', status = 303)

        #response = HttpResponse('my_data\t1111', content_type='application/vnd.ms-excel')
        #response['Content-Disposition'] = 'attachment; filename = "foo.xls"'
        #return response
        
        #response = JsonResponse({
        #    'keyk': 'valuesv',
        #    'key1': 'values1'
        #    })
        #return response

        #response = FileResponse(open('course/static/course/images/background.gif', 'rb'))
        #return response

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attchement; filename = "test.csv"'
        writer = csv.writer(response)
        writer.writerow(['111', '222', '3333', 'aaaa bbbb', '1111,2222'])
        writer.writerow(['111', '222', '3333', 'cccc bbbb', 'gggg,qqqq'])
        return response
    else:
        return HttpResponseNotFound("fdsfdsfdsfdsfds")
