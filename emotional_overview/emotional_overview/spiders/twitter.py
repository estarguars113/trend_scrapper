# -*- coding: utf-8 -*-
from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy.conf import settings
from scrapy import http
from emotional_overview.items import EmotionalOverviewItem

import json


class TwitterSpider(Spider):
    name = 'twitter'
    allowed_domains = ['twitter.com']


    def __init__(self, query='', lang=''):

        self.query = query
        self.url = "https://twitter.com/search?l=&q={0}&src=typd&lang={1}".format(query, lang)

     
    def start_requests(self):
        yield http.Request(self.url, callback= self.parse_page)


    def parse_page(self, response):
        data = json.loads(response.body.decode("utf-8"))
        for item in response.css('.stream-item').extract():
            description = item.css('.tweet-text').extract_first()
            link = item.css('.TwitterCard-container--clickable::attr(href)').extract_first()
            date = item.css('.tweet-timestamp::attr(data-original-title)').extract_first()
            user = item.css('.username').extract_first() 
    