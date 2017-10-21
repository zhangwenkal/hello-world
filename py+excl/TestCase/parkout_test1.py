#coding=utf-8
__author__ = 'Administrator'
import unittest,json,sys,time
sys.path.insert(1,"..")
from public.TestApi import testApi,testcookie
from public.read_excel import readExcel
from public.log import LogHelper
import requests

log=LogHelper('parkout').add_loger()

class testparkout(unittest.TestCase):

    def setUp(self):
        excel = readExcel('testcase.xls','parkout')
        self.name = excel.getNo
        self.data = excel.getData
        self.url = excel.getUrl
        self.method = excel.getMethod
        self.result=excel.getResult
        self.code = excel.getCode
        self.row = excel.getRows

    def testlogin(self):
        '''测试登录'''
        try:
            api = testcookie(self.method[0], self.url[0],self.data[0])
            log.info(' 发送请求')
            global api_cookie
            api_cookie=api.getCookie()
            log.info('获取cookie值')
        except Exception as ex:
            log.error(str(ex))

    def testparkout(self,method,url,api_cookie,**data):
        '''测试出场查询接口'''
        try:
            api = testApi(method,url,data,api_cookie)
            log.info(' 发送请求')
            apicode = api.getCode()
            log.info('获取响应状态')
            apijson = api.getJson()
            log.info('获取响应值')
            if apicode==self.code:
                self.assertEqual(apijson['actualBalanceTotal'], eval(self.result)['parkoutListCount'])  #eval,json.loads字符串转换成字典
                log.info('对比响应结果')
        except Exception as ex:
            log.error(str(ex))
    for i in range(1, self.row-1):
        testparkout(self.method[i],self.url[i],self.data[i],api_cookie)

if __name__ == '__main__':
    unittest.main(verbosity=2)
