# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from datetime import datetime

class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #房间名字
    room_name = scrapy.Field()
    #主播名字
    nick_name = scrapy.Field()
    #主播房间封面SRC
    image_src = scrapy.Field()
    #所在城市
    city = scrapy.Field()

    #图片路径
    image_path = scrapy.Field()

    utc_time = scrapy.Field()

    source = scrapy.Field()

