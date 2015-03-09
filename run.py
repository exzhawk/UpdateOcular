# -*- encoding: utf-8 -*-
# Author: Epix
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from UpdateOcular.spiders.Dospy import Dospy
from scrapy.utils.project import get_project_settings

spider = Dospy()
settings = get_project_settings()
crawler = Crawler(settings)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run()
print('stopped')