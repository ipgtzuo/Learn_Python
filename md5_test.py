#encoding = utf8
import hashlib

content1 = open('E:/tmp/test/a', 'rb').read()
md5_1 = hashlib.md5(content1).hexdigest()
print md5_1