# -*- coding: utf-8 -*-
__author__ = 'nolan'

import urllib2
import urllib
import re
import time
import os
import uuid

#获取二级页面
def findUrl2(html):
    rel = r'http://tuchong.com/\d+/\d+/ | http://\w+(?<!photos>.tuchong.com/\d+/)'
    url2List = re.findall(rel, html)
    url2lstfltr = list(set(url2list))
    url2lstfltr.sort(key=url2List.index)
    return url2lstfltr

def getHtml(url):
    html = urllib2.urlopen(url).read().decode('utf-8')
    return html

def download(html_pages, pageNo):
    x = time.localtime(time.time())
    foldername = str(x.__getattribute('tm_year')) + '-' + str(x.__getattribute__(tm_mon)) + '-' + str(x.__getattribute__(tm_mday))
    re2 = r'http://xxx'
    imglist = re.findall(re2, html_pages)
    print imglist

    for imgurl in imglist:
        picpath = 'H:\\ImageDownload\\%s\\%s' % (foldername, str(pageNo))
        filename = str(uuid.uuid1())




if __name__ == '__main__':
    print '''
            ******************************
            *  welcome to ...            *
            *                            *
            ******************************
        '''

    pageNo = raw_input("Please input page number:")
    while not pageNo.isdigit() or int(pageNo) > 100:
        if pageNo == 'quit':
            quitit()
        print "invalid page number, pleaswe try again!"
        pageNo = raw_input("Please input the page number you want to scratch:")

    html = getHtml("http://tuchong.com/tags/xxxxx/?page=" + str(pageNo))

    detllst = findUrl2(html)
    for detail in detllst:
        html2 = getHtml(detail)
        download(html2, pageNo)
    print "Finished!"