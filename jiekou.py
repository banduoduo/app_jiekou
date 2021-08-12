import requests
from   tcl import *

def get_cookie():
        urls = "http://182.92.178.83:8088/api/user/login"
        body_date = {"userName":"admin","password":"123456"}
        header_dict = {"Content-Type":"application/json"}
        rel_url = requests.post(urls,headers = header_dict,json = body_date)
        cookie = requests.utils.dict_from_cookiejar(rel_url.cookies)
        session = cookie['SESSION']

        return session