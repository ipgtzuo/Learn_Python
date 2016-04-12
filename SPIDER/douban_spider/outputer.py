# --*-- coding: utf-8 --*--
import codecs


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





