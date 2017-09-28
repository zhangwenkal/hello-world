import unittest,json,sys,time
sys.path.insert(1,"..")
from public.TestApi import testApi
from public.read_excel import readExcel
import requests

class testparkout(unittest.TestCase):
    def testparkout(self):
        '''测试出场查询接口。'''
        excel = readExcel('testcase.xls','parkout')
        name = excel.getNo
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        #uid = excel.getUid
        result=excel.getResult
        code = excel.getCode
        row = excel.getRows
        for i in range(0, row - 1):
            if i==0:
                api = testApi(method[i], url[i],data[i])
                api_cookie=api.getCookie()
            else:
                api = testApi(method[i],url[i],data[i],cookies=api_cookie)
                apicode = api.getCode()
                apijson = api.getJson()
            # if apicode==code[i] and apijson==result[i]  :
            #     print('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            # else:
            #     print('{}、{}:测试失败'.format(i + 1, name[i]))
                if apicode==code[i]:
                    self.assertEqual(apijson, json.loads(result[i]))


if __name__ == '__main__':
    unittest.main(verbosity=2)