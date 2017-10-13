import requests
import json

class testApi(object):
    def __init__(self, method,url,data,cookies):
        self.method = method
        self.url = url
        self.data = data
        self.cookies=cookies


    @property
    def testApi(self):
        # 根据不同的访问方式来访问接口
        if self.method == 'post':
            r=requests.post(self.url,data=eval(self.data),cookies=self.cookies)
            return r

            # except TimeoutError as ex:
            #     print('')
            #     print("Time out!")
            #     self.logger.error("Time out!")
        elif self.method == 'get':
            try:
                r = requests.get(self.url, params=eval(self.data))
                return r
            except TimeoutError:
                print("Time out!")


    def getCode(self):
        # 获取访问接口的状态码
        #code = self.testApi.json()['error']
        code = self.testApi.status_code
        return code

    def getJson(self):
        # 获取返回信息的json数据
        json_data = self.testApi.json()
        return json_data

class testcookie():
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data

    @property
    def testcookie(self):
        # 根据不同的访问方式来访问接口
        if self.method == 'post':
            try:
                r = requests.Session()
                r.post(self.url,data=eval(self.data))
                return r
            except TimeoutError:
                print("Time out!")
                # self.logger.error("Time out!")
        elif self.method == 'get':
            try:
                r = requests.get(self.url, params=eval(self.data))
                return r
            except TimeoutError:
                print("Time out!")

    def getCookie(self):
        # 获取返回信息的cookie
        cookie = self.testcookie.cookies
        return cookie