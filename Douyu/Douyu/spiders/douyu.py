# -*- coding: utf-8 -*-
import json
from Douyu.items import DouyuItem
import scrapy


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    offset = 0
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    start_urls = [base_url + str(offset)]
    unm = 0
    def parse(self, response):
        # print "###"*20
        # print type(response)
        # print response.body
        # print "###" * 20
        data_list = json.loads(response.body)['data']
        if not len(data_list):
            return
        for data in data_list:
            item = DouyuItem()
            # 房间名字
            item['room_name'] = data["room_name"]
            # 主播名字
            item['nick_name'] = data["nickname"]
            # 主播房间封面
            item['image_src'] = data['vertical_src']
            # 所在城市
            item['city'] = data['anchor_city']

            self.unm += 1
            print "写入第%s个" % self.unm
            yield item

        self.offset +=100
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)


