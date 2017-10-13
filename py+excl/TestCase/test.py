#coding=utf-8
__author__ = 'Administrator'
import requests,json
payload={"userName":"admin","password":"123456","veriCode":"8888"}

data={"_search":"false","nd":"","page.pageSize":"20","page.pageIndex":"1","page.sidx":"outTime","page.sord":"desc","keyword":"00000000","startTime":"2017-10-06 18:39:10","endTime":"2017-10-13 18:39:10","mod":"basic","filters":"null"}


s = requests.Session()
s.post("http://127.0.0.1:8080/jsds/security/app/login.do", data=payload)
cookies1=s.cookies  #['JSESSIONID']

print(cookies1)

r = requests.post('http://127.0.0.1:8080/jsds/park/app/parkoutListTotal.do',data,cookies=cookies1)

print(r.json())
print(type(r.json()))

print(s.cookies['JSESSIONID'])

#print(s.cookies)

