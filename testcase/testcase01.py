# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/13 17:00
# @filename :testcase01.py
# 开发工具 ：PyCharm
from ddt import *
import unittest
from BeautifulReport import BeautifulReport
from util import operation_excel
from util import runmethod
data1=operation_excel.OperationExcel().get_xls("userCase.xlsx", "login")
print(data1,type(data1))
from BeautifulReport import BeautifulReport
from HTMLTestReportCN import HTMLTestRunner
@ddt
class api_test(unittest.TestCase):
    def setUp(self):
        self.run_main=runmethod.RunMethod()
    @data(*data1)
    @unpack
    def test_run(self,casename,path,query,method):
        '''接口自动化测试'''
        url="http://127.0.0.1:8888"+path
        res=self.run_main.run_main(method=method,url=url,data=query)
        print(res.url)
        print(res.json())
        print(method)
        print(query)
        data1 = {"name": "xiaoming", "pwd": "111"}
        headers = {"content-type": "application/x-www-form-urlencoded"}
        res = self.run_main.run_main("Post", "http://127.0.0.1:8888/login", data=data1)
        print(res)
       # BeautifulReport.add_tester('测试者名称')

if __name__=="__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(api_test)  # 运行测试并生成报告
    br = BeautifulReport(test_suite)
    br.report(filename='report.html', description='Test Report')
