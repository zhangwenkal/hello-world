__author__ = 'Administrator'
import requests,json
payload={"userName":"admin","password":"123456","veriCode":"8888"}

s = requests.Session()
s.post("http://127.0.0.1:8080/jsds/security/app/login.do", data=payload)

print(s.cookies['JSESSIONID'])
#print(type(s.cookies))

