# --*-- coding: utf-8 --*--

import urllib2
import codecs
import urlparse

import pymongo
from bs4 import BeautifulSoup
import re
import time


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
        links = soup.find_all('a', href=re.compile(r"https://movie.douban.com/subject/\d*"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # soup = soup.prettify().encode('utf-8')
        # with open('html_cont.txt', 'wb') as f:
        #     f.writelines(soup)
        if soup:
            title = soup.find('span', property="v:itemreviewed")
            year = soup.find('span', class_='year')
            director = soup.find('span', class_='attrs')
            rating_num = soup.find('strong', property="v:average")

            if title and year and director and rating_num:
                if title.string and year.string and director.string and rating_num.string:
                    res_data['title'] = title.string
                    res_data['year'] = year.string[1:-1]
                    res_data['director'] = director.string
                    res_data['rating_num'] = rating_num.string

            return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data


class MongoDBIO:
    # 申明相关的属性
    def __init__(self, host, port, name, password, database, collection):
        self.host = host
        self.port = port
        self.name = name
        self.password = password
        self.database = database
        self.collection = collection

    # 连接数据库，db和posts为数据库和集合的游标
    def Connection(self):
        # connection = pymongo.MongoClient() # 连接本地数据库
        connection = pymongo.MongoClient(host=self.host, port=self.port)
        # db = connection.datas
        db = connection[self.database]
        if self.name or self.password:
            db.authenticate(name=self.name, password=self.password) # 验证用户名密码
        # print "Database:", db.name
        posts = db[self.collection]
        # print "Collection:", posts.name
        return posts



class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if len(data) != 0:
            self.datas.append(data)

    def output_html(self):
        # fout = open('output.txt', 'w')
        # for data in self.datas:
        #     if data['title'] and data['year'] and data['director'] and data['rating_num']:
        #     fout.write(data['title'])
        #     fout.write(data['year'])
        #     fout.write(data['director'])
        #     fout.write(data['rating_num'])
        #     fout.write("\n")

        import csv
        csvfile = open('douban_film.csv', 'wb')
        csvfile.write(codecs.BOM_UTF8)

        writer = csv.writer(csvfile)
        writer.writerow(['影片', '年份', '导演', '评分'])

        for data in self.datas:
            value = [data['title'], data['year'], data['director'], data['rating_num']]
            # print "******", value
            writer.writerow(value)

        csvfile.close()



class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            print "[craw %d]: %s" % (count, new_url)

            html_cont = self.downloader.download(new_url)
            new_url, new_data = self.parser.parse(new_url, html_cont)

            print "[new_data]: ", new_data

            self.urls.add_new_urls(new_url)
            self.outputer.collect_data(new_data)

            # if count == 1000:
            #     break
            count += 1

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://movie.douban.com/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

