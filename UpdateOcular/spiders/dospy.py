# -*- encoding: utf-8 -*-
# Author: Epix

import scrapy


class Dospy(scrapy.Spider):
    name = 'Dospy'

    def __init__(self, url, **kwargs):
        super(Dospy, self).__init__(**kwargs)
        self.start_urls = [url]

    def parse(self, response):
        o = open('t.txt', 'w')
        o.write('\n'.join(response.xpath('//div[@class="bm_c bt"]/a/text()').extract()))
        o.close()

