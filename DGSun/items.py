# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DgsunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DGItem(scrapy.Item):
    title = scrapy.Field()
    num =scrapy.Field()
    contect = scrapy.Field()
    url = scrapy.Field()