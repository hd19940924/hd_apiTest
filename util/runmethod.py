#coding:utf-8
import requests
import json
class RunMethod():
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:	
			res = requests.post(url=url,data=data,headers=header,verify=False)
		else:
			#res = requests.post(url=url,data=data)
			res=requests.post(url=url,data=json.dumps(data),verify=False)
			#return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
			#print(res.status_code)
		#return res
		return res

	def get_main(self,url,header=None,data=None):
		res = None
		if header !=None:	
			res = requests.get(url=url,params=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,params=data,verify=False)
			#print(res.status_code)
		return res
		#return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		return res
		#return json.dumps(res,ensure_ascii=False)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
if __name__=="__main__":
	R=RunMethod()
	data1={"name": "xiaoming","pwd": "111"}
	headers = {"content-type": "application/x-www-form-urlencoded"}
	res=R.run_main("Post","http://127.0.0.1:8888/login",data=data1)
	print(res)
	import requests
	url = "http://127.0.0.1:8888/login"
	querystring = {"name": "xiaoming", "pwd": "111"}
	payload = "name=xiaoming&pwd=111"
	headers = {"content-type": "application/x-www-form-urlencoded"}
	response = requests.request("POST", url, data=payload, headers=headers,params=querystring)
	print(response.text)


