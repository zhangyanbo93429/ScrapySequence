# -*- coding: utf-8 -*-
import scrapy
from sequence.items import SequenceItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://www.csdn.net/']

    def parse(self, response):
        for i in range(1,10):
            item = SequenceItem()
            item['name'] = i
            print('parsing'+str(item['name']))
            yield item
        pass
