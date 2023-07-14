# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/14 11:00
# @filename :Run_all_HTMLRunner.py.py
# 开发工具 ：PyCharm
from testcase.testcase01 import api_test
from BeautifulReport import BeautifulReport
import unittest
import time
if __name__ == '__main__':
    print(type(api_test))
    suite =unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(api_test))
    a =time.strftime("%Y-%m-%d %H_%M_%S")
    fp="C:/Users/admin/PycharmProjects/hd_apiTest/report/"+a+'_result.html'
    result = BeautifulReport(suite)
    result.report(filename='测试报告', description='测试报告', report_dir='C:/Users/admin/PycharmProjects/hd_apiTest/report', theme='theme_default')