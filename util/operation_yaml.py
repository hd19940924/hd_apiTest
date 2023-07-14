# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/13 10:18
# @filename :operation_yaml.py
# 开发工具 ：PyCharm
import os
import yaml   #读取
from util.operation_encrypt import MyClass
obj=MyClass()
class YamlUtil():
# 读取
     def read_yaml(self,key):
         with open( '../data/test.yaml', encoding='utf-8', mode='r') as f:
             data = yaml.load(f, yaml.FullLoader)
             value = data[key]
             if value.startswith("${md5(") and value.endswith(")}"):
                 password = value[7:-2]  # 去除前缀"${md5("和后缀")}"
                 encrypted_password = obj.md5(password)
                 return encrypted_password
             else:
                 return data
             #return value[key]
# 写入
     def write_yaml(self,data):
         with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='a') as f:
             yaml.dump(data, stream=f, allow_unicode=True)
# 清空
     def clear_yaml(self):
         with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='w') as f:
             f.truncate()
# 读取测试用例
     def read_testcase(self,yaml_name):
             with open(os.getcwd() + '\\testcases\\' + yaml_name, mode='r', encoding='utf-8') as f:
                 value = yaml.load(f, yaml.FullLoader)
                 return value
ya=YamlUtil()
password=ya.read_yaml("password")
print(password)#输出：${md5(password)}