# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs, json

class DgsunPipeline(object):
    def process_item(self, item, spider):
        return item

class JsondongguanPipelines(object):
    def __init__(self):
        #创建一个只读的文件，编码格式为utf-8
        self.filename = codecs.open('dongguan.json','w',encoding='utf-8')

    def process_item(self,item,spider):
        content = json.dumps(dict(item), ensure_ascii=False)+'\n'
        self.filename.write(content)
        return item
    def closed(self,spider):
        self.closed()
