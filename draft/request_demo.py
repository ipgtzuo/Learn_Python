
import requests
import json

Base_url = "http://10.3.31.232/rest/"

#Create a new user
def bugzilla_create_user(email, full_name, password, token):
    url = Base_url + "user"
    param = {"token": token, "email": email, "full_mame": full_name, "password": password}
    r = requests.post(url, params=param)

    ret = json.loads(r.text)
    print ret
    id = ret['result']['id']

    return id

#Login with a exiting user
def bugzilla_login(email, password):
    url = Base_url + "login"
    param = {"login": email, "password": password}
    r = requests.get(url, params=param)

    ret = json.loads(r.text)
    id = ret['result']['id']
    token = ret['result']['token']

    return id, token

def bugzilla_logout(token):
    url = Base_url + "logout"
    param = {"token":token}
    requests.get(url, params=param)

def bugzilla_create_product(name,description,version,):
    url = Base_url + "product"
    param = {"name":name}
    requests.get(url, params=param)

def bugzilla_get_all_bug():
    url = Base_url + "bug"
    r = requests.get(url)

    ret = json.loads(r.text)

    bugs = ret['result']['bugs']
    # for bug in bugs:
    #     print "ID = ",bug['id']
    #     print "Creator = ",bug['creator']
    #     print "Creation_time = ",bug['creation_time']
    #     print "Status =" ,bug['status']
    #     print "Product = " ,bug['product']
    #     print "Component = " ,bug['component']
    #     print "Summary = " ,bug['summary']
    #     print ""

    return bugs

def test_api():
    # id,token = bugzilla_login("jiangh_os@sari.ac.cn","123456")
    # print "Login result:%s %s" % (id,token)
    # id = bugzilla_create_user("yangqh_os@sari.ac.cn","yangqihang","123456",token)
    # print "New user ID" id
    # bugzilla_logout(token)
    bugs = bugzilla_get_all_bug()
    for bug in bugs:
        print "ID = ",bug['id']
        print "Creator = ",bug['creator']
        print "Creation_time = ",bug['creation_time']
        print "Status =" ,bug['status']
        print "Product = " ,bug['product']
        print "Component = " ,bug['component']
        print "Summary = " ,bug['summary']
        print ""

if __name__ == "__main__":
    test_api()

