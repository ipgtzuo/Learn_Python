# --*-- encoding = utf-8 --*--

import sys
import requests


Base_url = "http://127.0.0.1:8000/api/article/article/"
get_key_url = "http://127.0.0.1:8000/account/getUserKey/"
register_url = "http://127.0.0.1:8000/api/account/user/CreateUser/"
create_forum_url = "http://127.0.0.1:8000/api/forum/forum/"
create_district_url = "http://127.0.0.1:8000/api/district/district/"

def get_user_key(username):
    url = get_key_url
    param = {"username": username}
    r = requests.get(url, params=param)
    return r.content


def get_article_by_username(user_auth):
    user_name = user_auth['username']
    url = Base_url + "?user__username=" + user_name
    r = requests.get(url, params=user_auth)
    print r.content
    return r.json()


def get_article_by_forum(forum, user_auth):
    url = Base_url + "?forum__name=" +forum
    r = requests.get(url, params=user_auth)
    print r.content

    return r.json()


def post_new_article(title, content, forum_id, user_auth):
    url = Base_url
    forum = "/api/forum/forum/" + forum_id +"/"

    data = {
        "title": title,
        "forum": forum,
        "body": content,
    }

    r = requests.post(url, json=data, params=user_auth)

    print r.content

    return r.json()

def register(new_user, password):
    url = register_url
    r = requests.post(url, json={"username": new_user, "password": password})
    print r.content
    return r.content

def new_forum(forum_name, description, district, api_key):
    url = create_forum_url + "?username=root&?api_key=" + api_key

    data = {
        "name": forum_name,
        "description": description,
        "district": district,
    }

    r = requests.post(url, json=data)
    return r.content


def new_district(district_name, description, api_key):
    url = create_district_url + "?username=root&?api_key=" + api_key

    data = {
        "name": district_name,
        "description": description,
    }

    r = requests.post(url, json=data)
    return r.content


def main():
    try:
        if sys.argv[1] == 'username':
            user_name = sys.argv[2]
            api_key = get_user_key(user_name)
            user_auth = {"username": user_name, "api_key": api_key}
            get_article_by_username(user_auth)
        if sys.argv[1] == 'forum':
            user_name = "TEST"
            api_key = get_user_key(user_name)
            user_auth = {"username": user_name, "api_key": api_key}
            get_article_by_forum(sys.argv[2], user_auth)
        if sys.argv[1] == 'new_user':
            user_name = sys.argv[2]
            api_key = get_user_key(user_name)
            user_auth = {"username": user_name, "api_key": api_key}
            # title = "ApiTest"
            # content = "Hello, Api test!"
            # forum_id = "4"

            title = sys.argv[3]
            content = sys.argv[4]
            forum_id = sys.argv[5]

            post_new_article(title, content, forum_id, user_auth)

        if sys.argv[1] == 'new_forum':
            user_name = "root"
            api_key = get_user_key(user_name)
            forum_name = sys.argv[2]
            description = sys.argv[3]
            district = sys.argv[4]
            new_forum(forum_name, description, district, api_key)

        if sys.argv[1] == 'new_district':
            user_name = "root"
            api_key = get_user_key(user_name)
            district_name = sys.argv[2]
            description = sys.argv[3]
            new_district(district_name, description, api_key)

        elif sys.argv[1] == 'register':
            new_user = sys.argv[2]
            password = sys.argv[3]
            register(new_user, password)

        else:
            print '''
                 usage: 1. Search article by user_name:  python bbs_api_search.py username [user_name]
                        2. Search article by forum_name:  python bbs_api_search.py forum [forum_name]
                        3. Post new article:  python bbs_api_search.py new_user [user_name] [title] [content] [forum_id]
                        4. Create new user: python bbs_api_search.py register [username] [password]
                        5. Create new forum: python bbs_api_search.py new_forum [forum_name] [description] [district]
                        6. Create new district python bbsa_api_search.py new_district [district_name] [description]
            '''
    except Exception, e:
        print e


if __name__ == "__main__":
    main()
