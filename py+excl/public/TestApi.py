import requests
import json

class testApi(object):
    def __init__(self, method, url, data):
        self.method = method
        self.url = url
        self.data = data


    @property
    def testApi(self):
        # 根据不同的访问方式来访问接口
        if self.method == 'post':
            try:
                r = requests.post(self.url, data=json.dumps(self.data))
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


    def getCode(self):
        # 获取访问接口的状态码
        #code = self.testApi.json()['error']
        code = self.testApi.status_code
        return code

    def getJson(self):
        # 获取返回信息的json数据
        json_data = self.testApi.json()
        return json_data