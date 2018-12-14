# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmotionalOverviewItem(scrapy.Item):
    title = scrapy.Field()
    source = scrapy.Field()
    description = scrapy.Field()
    related_link = scrapy.Field()
    created_date = scrapy.Field()
    tags = scrapy.Field()
    user = scrapy.Field()