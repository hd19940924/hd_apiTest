# _*_coding:utf-8_*_
# @Author :hd
# @time :2023/7/12 17:23
# @filename :jiami.py
# 开发工具 ：PyCharm
# MD5加密
import base64
import hashlib
import rsa
class MyClass():
  def md5(self,args=None):
    if args is None:
        md5_str=''
        return md5_str  # 返回为小写，需要转大写后面添加.upper
    else:
        utf8_str = str(args).encode("utf-8")
        # md5加密（哈希算法）
        md5_str = hashlib.md5(utf8_str).hexdigest()
        return md5_str  # 返回为小写，需要转大写后面添加.upper
        # BASE64加密
  def bs64(self, args):
    # 以指定的编码格式编码字符串
        utf8_str = str(args).encode("utf-8")         # base64加密
        base64_str=base64.b64encode(utf8_str).decode("utf-8")
        #base64.b64encode(utf8_str)是字节格式，使用decode(         # "utf-8")将其转换成字符串
        return base64_str  # 返回为小写，需要转大写后面添加.upper       #RSA双密钥加密方式     #生成公钥的私钥写入到指定的pem文件：
  def create_key(self):         #根据密钥长度生成公钥和私钥
        (public_key,private_key)=rsa.newkeys(1024)
        print(public_key,private_key)
        #保存公钥
        with open("D:\\测试项目\\接口测试自动化2\\public.pem","w+") as f:
            f.write(public_key.save_pkcs1().decode())
            # 保存私钥
        with open("D:\\测试项目\\接口测试自动化2\\private.pem","w+") as f:
            f.write(private_key.save_pkcs1().decode())       #通过公钥加密
  def public_key_jiami(self,args):         # 导入密钥
         with open("public.pem") as f:
             pubkey= rsa.PublicKey.load_pkcs1(f.read().encode())
             #加密
         byte_str=rsa.encrypt(str(args).encode("utf-8"),pubkey)
         print(byte_str)         #把二进制转换成字符串格式
         miwen =base64.b64encode(byte_str).decode('utf-8')
         return miwen       #通过私钥解密
  def private_key_jiemi(self,args):         # 导入私钥
     with open("private.pem") as f:
         prikey = rsa.PrivateKey.load_pkcs1(f.read().encode())         #解密
     byte_str=base64.b64decode(args)
     mingwen=rsa.decrypt(byte_str,prikey).decode()
     return mingwen
"""obj=MyClass()
password = "999"
encoded_password =obj.bs64(password)
print(encoded_password)  # 输出：OTk5"""