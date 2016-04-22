
# --*-- coding: utf-8 --*--

import urllib2
# import codecs
import urlparse

# import pymongo
from bs4 import BeautifulSoup
import re
# import time


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if (url not in self.new_urls) and (url not in self.old_urls):
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


class HtmlDownloader(object):
    def __init__(self):
        pass

    def download(self, url):
        if url is None:
            return None

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        data = None
        request = urllib2.Request(url, data, headers)

        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None

        return response.read()


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"http://zz.fang.anjuke.com/.*?"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls




class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        f = open('url_collection.txt', 'w+')

        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print "[craw %d]: %s" % (count, new_url)
            f.writelines(new_url)
            f.writelines('\n')

            html_cont = self.downloader.download(new_url)
            new_url = self.parser.parse(new_url, html_cont)

            self.urls.add_new_urls(new_url)

            # if count == 1000:
            #     break
            count += 1
        f.close()


if __name__ == "__main__":
    root_url = "http://zz.fang.anjuke.com/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)