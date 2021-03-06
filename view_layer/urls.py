# -*- coding: utf-8 -*-
"""view_layer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from course import urls as course_urls
from course import views as course_views
from . import views as root_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^course/', include(course_urls)),
    url(r'^course/', include('course.urls')),
]

# 自定义错误页面,在其它app中的二级URLconf中设置这些变量无效。
# 经测试以下配置无效
handler400 = root_views.bad_request
handler403 = root_views.permission_denied
handler404 = root_views.page_not_found
handler500 = root_views.page_error
