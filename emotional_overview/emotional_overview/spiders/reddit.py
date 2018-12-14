# -*- coding: utf-8 -*-
from scrapy.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy.conf import settings
from scrapy import http
from emotional_overview.items import EmotionalOverviewItem

import json


class RedditSpider(Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/']

    def __init__(self, query='', lang=''):

        self.query = query
        self.url = "https://www.reddit.com/search?q={0}&type=link".format(query)

     
    def start_requests(self):
        yield http.Request(self.url, callback= self.parse_page)


    def parse_page(self, response):
        data = json.loads(response.body.decode("utf-8"))
        for item in response.css('.scrollerItem').extract():
            title = item.css('a>h2>span').extract_first()