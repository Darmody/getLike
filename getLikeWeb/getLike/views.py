#coding=utf-8
#-*- coding: UTF-8 -*-


from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from getLike.models import Drama

def hello(request) :

    return HttpResponse("Hello world")

#获取美剧更新方法
def getDrama(request) :
    #数据库获取Drama对象
    dramas = Drama.objects.all()
    #循环处理所有对象
    for drama in dramas :
        #unicode解码
        s = drama.episodeName.decode('unicode_escape')
        drama.episodeName = s.split('\'')[1].strip()   #处理集名
        drama.downloadLink = drama.downloadLink[3 : len(drama.downloadLink) - 3]    #处理下载链接
    #指向模板
    t = get_template('getDrama.html')
    #带入参数
    html = t.render(Context({'dramas' : dramas}))

    return HttpResponse(html)