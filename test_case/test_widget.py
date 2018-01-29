#coding=utf-8
from interface.widget import Widget
import unittest
import re
'''测试对应request,所有响应的取值和断言全在这里写'''

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.weight = Widget()

    def testSize(self):
        self.assertEquals(self.weight.get_size(), (40, 40))

    def testResize(self):
        self.weight.resize(100,120)
        self.assertEquals(self.weight.get_size(), (100, 120))

    def testlogin(self):
        self.assertEquals(self.weight.login().json()['name'],"李老师".decode('utf-8'))


    def tearDown(self):
        self.weight = None

if __name__ == "__main__":
    unittest.main()
