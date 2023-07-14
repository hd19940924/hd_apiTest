# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/13 10:48
# @filename :test_bs4.py
# 开发工具 ：PyCharm
import base64
class MyClass():
    def bs64(self, args):         # 以指定的编码格式编码字符串
         utf8_str = str(args).encode("utf-8")         # base64加密
         base64_str = base64.b64encode(utf8_str).decode("utf-8")         #
         # base64.b64encode(utf8_str)是字节格式，使用decode("utf-8")将其转换成字符串
         return base64_str  # 创建实例对象
obj = MyClass()
password = "999"
encoded_password = obj.bs64(password)
print(encoded_password)  # 输出：OTk5