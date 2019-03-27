# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DGSun.items import DGItem

class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    #每个页面的匹配规则
    pagelink = LinkExtractor(allow=('/question/report'))
    print(pagelink)

    #每个帖子的匹配规则
    contentlink = LinkExtractor(allow=('/html/question/\d+/\d+.shtml'))

    rules = [
        Rule(pagelink, follow=True ),
        Rule(contentlink, callback='parse_item')
    ]


    def parse_item(self, response):
        # print(response.url)
        title = response.xpath("//span[@class='niae2_top']/text()").extract()[0].replace("提问：","")

        # print(title)
        num = response.xpath("//tr/td[2]/span[2]/text()").extract()[0].split(":")[-1]
        # print(num)

        contect = response.xpath("//td[@class='txt16_3']/text()").extract()
        contect = "".join(contect)
        contect = contect.replace('\xa0\xa0\xa0\xa0','').replace('\r\n      ','').replace('\n','')

        # print(contect)


        item = DGItem()

        item['title'] = title
        item['num'] = num
        item['contect'] = contect
        item['url'] = response.url


        print(item)
        yield item