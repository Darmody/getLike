#coding=utf-8
#-*- coding: UTF-8 -*-

'''
Created on 2014年4月4日

@author: caihuanyu
'''

from scrapy.spider import Spider
from scrapy.selector import Selector

from getLikeScrapy.items import DramaItem

class GetDramaSpider(Spider):
    
    name = "getDrama"
    allowed_domains = ["yayaxz.com"]        #丫丫下载站
    start_urls = [
        "http://www.yayaxz.com/resource/10733"      #权利的游戏
    ]
    
    def parse(self, response):
        
        sel = Selector(response)
       
        resList = sel.xpath('//div[@class="resource-list-box"]/dl[@class="resource-list"]')
        resItems = resList.xpath('//dd[@class=" resource-item" and @data-season="4"] | //dd[@class="odd resource-item" and @data-season="4"]')     #获取第4季
           
        items = []
        
        for resItem in resItems : 
            
            item = DramaItem();
            #集名
            item['episodeName'] = resItem.xpath('a[not(@class="type")]/text()').extract()  
            #下载链接
            item['downloadLink'] = (resItem.xpath('span/a[@data-download-type="1"]/@href').extract())

            items.append(item)
            
        return items


