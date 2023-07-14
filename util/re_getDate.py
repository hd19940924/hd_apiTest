# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/14 11:21
# @filename :re_getDate.py
# 开发工具 ：PyCharm
import re
with open("../report/测试报告.html","r",encoding="utf-8") as f:
    report_content=f.read()
testAll_count=re.findall(r'"testAll"\s*:\s*(\d+)',report_content)[0]
testFail_count=re.findall(r'"testFail"\s*:\s*(\d+)',report_content)[0]
beginTime=re.findall(r'"beginTime"\s*:\s*"([^"]*)"',report_content)[0]
testSkip_count=re.findall(r'"testSkip"\s*:\s*(\d+)',report_content)[0]
testError_count=re.findall(r'"testError"\s*:\s*(\d+)',report_content)[0]
testPass_coumt=re.findall(r'"testPass"\s*:\s*(\d+)',report_content)[0]
print(testAll_count)
print(testFail_count)
print(beginTime)
print(testSkip_count)
print(testError_count)
print(testPass_coumt)
