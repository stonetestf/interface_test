#coding=utf-8

'''只写请求，返回响应，具体取值由test_case里面写'''
import requests


class Widget:
    def __init__(self,size=(40,40)):
        self._size = size

    def get_size(self):
        return self._size

    def resize(self, weight, height):
        if weight < 0 or height < 0:
            raise ValueError,"illegal size"
        self._size = (weight, height)

    def login(self):
        testurl = "http://qa.zgyjyx.net/api/teacher/mobile/login/"
        playload = {
            "username":"",
            "password":"",
            "ostype":"1",
            "devicetoken":"dedf34810faa97f361e8d377b65353027a0376d101b7a13cde7fe664fc67cd06"
        }
        res = requests.post(url=testurl, data=playload)
        return res
