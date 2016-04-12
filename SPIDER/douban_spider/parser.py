# --*-- coding: utf-8 --*--
import re
import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"https://movie.douban.com/subject/\d*/\?from=showing"))
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

