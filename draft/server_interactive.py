# --*-- coding = utf-8 --*--
__author__ = 'zhaoxu'

import datetime
import sys
import subprocess


SEARCHTIME = datetime.datetime.now()

def info_search(item):
    command = 'curl -H "Accept: application/json" http://127.0.0.1:8000/api/' + item +'/ | python -m json.tool'
    FILENAME = 'Search_BY_' + item + SEARCHTIME.strftime('_%Y%m%d%H%M%S')
    FILEPATH = '/home/nolan/Desktop/' + FILENAME
    search_result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    with open(FILEPATH, 'w') as f:
        for line in search_result.stdout.readlines():
            print line
            f.write(line)

def feedback_api_get_article_by_user(usr):
    return json

def main():
    try:
        if len(sys.argv) > 1:
            info_search(sys.argv[1])
        else:
            print '''
                 usage: python bbs_api_search.py XXXX
            '''
    except Exception, e:
        print e


if __name__ == "__main__":
    main()