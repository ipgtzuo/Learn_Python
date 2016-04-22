```python

def ContentSave(item):
    # 保存配置
    save_host = "localhost"
    save_port = 27017
    save_name = ""
    save_password = ""
    save_database = "textclassify"
    save_collection = "WallstreetcnSave"

    source = "wallstreetcn"
    createdtime = datetime.datetime.now()
    type = item[0]
    content = item[1].decode("unicode_escape") # json格式数据中，需从'\\uxxxx'形式的unicode_escape编码转换成u'\uxxxx'的unicode编码
    content = content.encode("utf-8")
    # print content
    # district的筛选
    categorySet = item[2]
    category_num = categorySet.split(",")
    category_name = map(num2name, category_num)
    districtset = set(category_name)&{u"中国", u"美国", u"欧元区", u"日本", u"英国", u"澳洲", u"加拿大", u"瑞士", u"其他地区"}
    district = ",".join(districtset)
    propertyset = set(category_name)&{u"外汇", u"股市", u"商品", u"债市"}
    property = ",".join(propertyset)
    centralbankset = set(category_name)&{u"央行"}
    centralbank = ",".join(centralbankset)
    save_content = {
        "source":source,
        "createdtime":createdtime,
        "content":content,
        "type":type,
        "district":district,
        "property":property,
        "centralbank":centralbank
    }
    ResultSave(save_host, save_port, save_name, save_password, save_database, save_collection, save_content)
```
