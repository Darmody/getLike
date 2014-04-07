#coding=utf-8
#-*- coding: UTF-8 -*-

from django.db import models

#美剧剧集对象
class Drama(models.Model):

    episodeName = models.CharField(max_length=32, unique=True)   #集名
    downloadLink = models.CharField(max_length=500)  #下载地址
