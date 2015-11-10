# encoding=utf-8
# __author_ _ = 'ZhaoXu'

import os

PY_ITEMS = [
    'jdcal', 
    'openpyxl', 
    'ecdsa',  
    'paramiko', 
    'pymongo', 
    'flup', 
    'M2Crypto', 
    'south', 
    'xlwt', 
    'redis', 
    'xlrd', 
    'dbfpy'
	'image'
]

FILE_MAP = {
	"haproxy" : r'/etc/init.d/haproxy',
	"redis" : r'/home/rzrk/redis',
	"lua" : r'/usr/local/share/lua',
}

def pyCheck(checkItems):
    lessModules = []
    for item in checkItems:
        try:
            command ="import "+item
            exec(command)        
        except Exception as e:
            lessModules.append(item)
    return lessModules
    

def fileCheck(fileMap):	
    lessModules = []
    for tag, filename in fileMap.iteritems():
	if not os.path.exists(filename):
            lessModules.append(tag)
    return lessModules
		
if __name__ == "__main__":
    lessModules = []
    lessModules.extend(pyCheck(PY_ITEMS))
    lessModules.extend(fileCheck(FILE_MAP))
    if len(lessModules) > 0:
        print "less modules : ", ",".join(lessModules)
    else:
        print "check pass"
    
    
