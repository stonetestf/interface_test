import json
import re

import requests

class Login:
    def login(self):
        testurl = "http://qa.zgyjyx.net/api/teacher/mobile/login/"
        playload = {
            "username":"",
            "password":"",
            "ostype":"1",
            "devicetoken":"dedf34810faa97f361e8d377b65353027a0376d101b7a13cde7fe664fc67cd06"
        }
        res = requests.post(url=testurl, data=playload)

        print res.json()['name']
        # print res.headers
        # print res.status_code
        # print res.text
        # print res.content
if __name__=="__main__":
    res1 = Login()
    res1.login()