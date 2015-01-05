# -*- coding: utf-8 -*-
import hashlib
import logging
import time, os
import cPickle
import uuid
import zipfile, cStringIO
import datetime
import requests, json
from pyatom import AtomFeed
from lxml import etree
from lxml.cssselect import CSSSelector
import codecs

__author__ = 'Epix'

# proxies = {'http': 'http://127.0.0.1:8088'}


def fetchURL(url):
    proxies = {'http': 'http://192.168.1.118:8087'}
    ua = {'User-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'}

    # return requests.get(url, verify=False, proxies=proxies)
    return requests.get(url, headers=ua, verify=False, timeout=30)


class mod:
    count = 0

    def __init__(self, id, url, option=''):
        self.id = id
        self.url = url
        self.option = option
        mod.count += 1

    def check(self):
        pass

class curseforge(mod):
    def check(self):
        modPage = fetchURL(self.url + '/files').text
        modHTML = etree.HTML(modPage)
        fileSel = CSSSelector('table.listing > tbody > tr:first-child> td.project-file-name > div > div.project-file-name-container > a')
        modFile = fileSel(modHTML)[0]
        # print(etree.tostring(modFile))
        fileName = modFile.text.strip()
        # print(fileName)
        modFile.set('href', 'http://minecraft.curseforge.com' + modFile.get('href')+'/download')
        self.tips = etree.tostring(modFile)
        # print(modFile.get('href'))
        filePage = fetchURL(modFile.get('href')[:-9]).text
        # print(filePage)
        fileHTML = etree.HTML(filePage)
        changelogSel = CSSSelector('div.logbox')
        changelog = changelogSel(fileHTML)[0]
        changelog.set('class', '')
        self.tips += '</br>' + etree.tostring(changelog)


c = [curseforge('Waila NBT', 'http://minecraft.curseforge.com/mc-mods/224417-waila-nbt')]
for ci in c:
    ci.check()
for ci in c:
    print(ci.tips)