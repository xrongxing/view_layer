# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,JsonResponse,FileResponse,StreamingHttpResponse
from django.template import loader, Context
import csv
from reportlab.pdfgen import canvas
# canvas 不支持中文，导入以下包
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont 
# 上传字体文件到/usr/share/fonts/目录
pdfmetrics.registerFont(TTFont('simkai', 'chinese/simkai.ttf'))

from io import BytesIO

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

        #response = HttpResponse(content_type='text/csv')
        #response['Content-Disposition'] = 'attchement; filename = "test.csv"'
        #writer = csv.writer(response)
        #writer.writerow(['111', '222', '3333', 'aaaa bbbb', '1111,2222'])
        #writer.writerow(['111', '222', '3333', 'cccc bbbb', 'gggg,qqqq'])
        #return response

        #以下示例有错误 
        #response = HttpResponse(content_type='text/csv')
        #response['Content-Disposition'] = 'attchement; filename = "test.csv" '
        #csv_data = (
        #    ('111', 'aaa', 'fdsaf', 'aaa  bbbb',),
        #    ('111', 'aaa', 'fdsfdsf', '11111,aaaa', "aaaa'aaaa", 'aaaaa"aaaaa',),
        #)
        #t = loader.get_template('course/templatecsv.txt')
        #c = Context({'data': csv_data,})
        #response.write(t.render(c))
        #return response
        #以上示例有错误
       
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'attachement, filename = "test.pdf" '
        #p = canvas.Canvas(response)
        ##p.drawString(100, 100, 'aaaa aaaa',)
        #p.drawString(10, 800, 'aaaa aaaa',)
        #p.showPage()
        #p.save()
        #return response
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachement, filename = "ttest.pdf"'
        Buffer = BytesIO()
        p = canvas.Canvas(Buffer)
        # 汉字有问题,需要导入相关包并上传字体
        p.setFont('simkai', 8)
        #p.drawString(100, 800, '测试 pdf 文字',)
        p.drawString(100, 800, u'测试 pdf 文字',)
        p.showPage()
        p.save()
        pdf = Buffer.getvalue()
        Buffer.close()
        response.write(pdf)
        return response

    else:
        return HttpResponseNotFound("fdsfdsfdsfdsfds")

class Echo(object):
    def write(self, value):
        return value

def some_streaming_csv_view(request):
    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),content_type='text/csv')
    response['Content-Disposition'] = 'attchement, filename = "test.csv" '
    return response
