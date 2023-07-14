import requests
"""     http工具类的封装 """
class RequestUtil():
    def __init__(self):
        pass
    def request(self, url, method, headers=None, param=None, content_type=None):
        """         通用请求工具类
        :param url:
        :param method:
        :param headers:
        :param param:
        :param content_type:
        :return:
        """
        try:
            if method == 'get':
                result = requests.get(url=url, params=param, headers=headers).json()
                return result
            elif method == 'post':
                     if content_type == "application/json":
                         result = requests.post(url=url, json=param, headers=headers).json()
                         return result
                     else:
                         result = requests.post(url=url, data=param, headers=headers).json()
                         return result
            else:
                         print("http method not allowed!!!")
        except Exception as e:
                        print("http请求错误:{0}".format(e))
if __name__ == "__main__":
   url = "https://api-v2.xdclass.net/api/order/v1/query_pay?productId=87"
   url1="https://www.baidu.com/"
   r = RequestUtil()
   result = r.request(url,"get",)
   print(result)
# post请求
   url = "https://api-v2.xdclass.net/api/comment/v1/page"
   data = {"page": "1", "size": "8", "bizId": "87"}
# application/x-www-form-urlencoded
   headers = {"Content-Type":"application/json"}
   r = RequestUtil()
   result = r.request(url, "post",param=data,content_type="application/json")
   print(result)
   data1 = {"name": "xiaoming", "pwd": "111"}
   result1=r.request(url="http://127.0.0.1:8888/login/",method="post",param=data1)
   #print(result1)
