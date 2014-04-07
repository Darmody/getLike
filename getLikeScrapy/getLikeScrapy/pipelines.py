#coding=utf-8
#-*- coding: UTF-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from getLike.models import Drama
from django.db.utils import IntegrityError

class GetlikescrapyPipeline(object):
    def process_item(self, item, spider):
        return item

class GetDramaPipeline(object) :
    def process_item(self, item, spider):
        #获取数据库中已有的数据
        drama = Drama.objects.filter(episodeName=item['episodeName'])
        #如果有数据
        if len(drama) > 0 :
            #执行更新
            drama[0].episodeName = item['episodeName']
            drama[0].downloadLink = item['downloadLink']

            drama[0].save()
        #如果没有数据，直接保存
        else :

            item.save()

        return item
