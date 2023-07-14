# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/13 13:50
# @filename :mock_tool.py
# 开发工具 ：PyCharm
#from mock import mock
import json
from unittest import mock
import unittest
from runmethod import RunMethod
#模拟mock 封装
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)
    #res=mock_method()
    res = mock_method(url,method,request_data)
    return res
#mock_test()
class TestMethod(unittest.TestCase):
 def setUp(self):
        self.run = RunMethod()

 def test_03(self):
    url = 'http://coding.imooc.com/api/cate'
    data = {
                    'timestamp':'1507034803124',
                    'uid':'5249191',
                    'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
                    'secrect':'078474b41dd37ddd5efeb04aa591ec12',
                    'token':'7d6f14f21ec96d755de41e6c076758dd',
                    'cid':'0',
                    'errorCode':1001
    }
    mock_data=mock.Mock(return_value=data)
    self.run.run_main=mock_data
   # self.run.run_main = mock.Mock(return_value=data)
    res = mock_test(self.run.run_main,data,url,"POST",data)
    print(res)
    #res = self.run.run_main(url,'POST',data)
    # #print(res)
    self.assertEqual(res['errorCode'],1001,"测试失败")
    print ("这是第一个case")

 def test_02(self):
     url = 'http://coding.imooc.com/api/cate'
     data = {
             'timestamp':'1507034803124',
             'uid':'5249191',
             'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
             'secrect':'078474b41dd37ddd5efeb04aa591ec12',
             'token':'7d6f14f21ec96d755de41e6c076758dd',
             'cid':'0'
             }
     res = self.run.run_main('POST',url,data).json()

     self.assertEqual(res['errorCode'],1001,"测试失败")
     print("这是第二个case")
if __name__=="__main__":
    unittest.main()
