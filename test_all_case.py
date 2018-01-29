#coding=utf-8
import HTMLTestRunner
import unittest
import os
import time

'''run and create report'''

# for case in os.listdir("D:\\software\\python_file\\practice"):
#     if case.endswith(".py"):
#         os.system("python " + case + " 1>>log.txt 2>&1")

suite = unittest.TestSuite()
#suite.addTest(unittest.makeSuite(test_widget.WidgetTestCase))
discover = unittest.defaultTestLoader.discover(os.path.join(os.getcwd(),"test_case\\"),
                                               pattern='test_*.py',
                                               top_level_dir=None)

for test_suite in discover:
    for test_case in test_suite:
        suite.addTest(test_case)



now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
filename = os.path.join(os.getcwd(), "report\\" + now + " result.html")
fp =file(filename, "wb")

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'test title',
    description=u'test description'
)

runner.run(suite)