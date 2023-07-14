# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/14 10:45
# @filename :Run_all.py
# 开发工具 ：PyCharm
import HTMLTestReportCN

from testcase.testcase01 import api_test
from util.HTMLTestRunner_PY3 import HTMLTestRunner

import unittest
import time
if __name__ == '__main__':
    print(type(api_test))
    suite =unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(api_test))
    a =time.strftime("%Y-%m-%d %H_%M_%S")
    fp="C:/Users/admin/PycharmProjects/hd_apiTest/report/"+a+'_result.html'
    with open(fp, 'w',encoding="utf-8",errors='ignore') as f:
        runner = HTMLTestRunner(stream=f,
                                                   title='测试报告',
                                                   description='测试用例的执行情况',
                                                   verbosity=2,tester="hd")
        runner.run(suite)

