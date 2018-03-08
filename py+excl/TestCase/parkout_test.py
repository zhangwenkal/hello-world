import unittest,json,sys,time
sys.path.insert(1,"..")
from public.TestApi import testApi,testcookie
from public.read_excel import readExcel
from public.log import LogHelper
import requests,os,datetime
from public.py_Html import createHtml
from public.panduan import assert_in
log=LogHelper('parkout').add_loger()

class testparkout(unittest.TestCase):
    def testparkout(self):
        '''测试出场查询接口。'''
        excel = readExcel('testcase.xls','parkout')
        No = excel.getNo
        data = excel.getData
        url = excel.getUrl
        method = excel.getMethod
        #uid = excel.getUid
        assert_result=excel.getResult
        code = excel.getCode
        row = excel.getRows

        #测试返回
        list_pass=0
        list_fail=0
        list_json=[]
        listresult=[]

        #测试报告
        starttime=datetime.datetime.now()
        day= time.strftime("%Y-%m-%d_%H_%M", time.localtime(time.time()))
        basdir=os.path.abspath(os.path.dirname(__file__))
        filepath =os.path.join(os.path.dirname(basdir)+'\\test_Report\\%s-result.html'%day)

        #执行测试用例
        for i in range(0, row-1):
            if i==0:
                try:
                    api = testcookie(method[i], url[i],data[i])
                    global api_cookie
                    api_cookie=api.getCookie()
                    api_code=api.getCode()
                    assert_re=assert_in(api_code,code[i])

                    if  assert_re=='pass':
                        list_json.append(api_code)
                        listresult.append('pass')
                        list_pass+=1
                    else:
                        list_fail+=1
                        listresult.append('fail')
                        list_json.append(api_code)
                    log.ingo('对比响应结果')

                except Exception as ex:
                    log.error(str(ex))

            else:
                try:
                    api = testApi(method[i],url[i],data[i],api_cookie)
                    log.info(' 发送请求')
                    apicode = api.getCode()
                    log.info('获取响应状态')
                    apijson = api.getJson()
                    log.info('获取响应值')
                    # if apicode==code[i]:
                    #     self.assertEqual(apijson['actualBalanceTotal'], eval(result[i])['actualBalanceTotal'])  #eval,json.loads字符串转换成字典
                    assert_re=assert_in(apijson,eval(assert_result[i]))
                    if  assert_re=='pass':
                        list_json.append(apijson)
                        listresult.append('pass')
                        list_pass+=1
                    else:
                        list_fail+=1
                        listresult.append('fail')
                        list_json.append(apijson)
                    log.ingo('对比响应结果')

                except Exception as ex:
                    log.error(str(ex))
            # if apicode==code[i] and apijson==result[i]  :
            #     print('{}、{}:测试成功。json数据为:{}'.format(i + 1, name[i], apijson))
            # else:
            #     print('{}、{}:测试失败'.format(i + 1, name[i]))
        #创建测试报告
        endtime=datetime.datetime.now()
        createHtml(titles='接口测试报告',filepath=filepath,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=No,name='',key='',coneent=data,url=url,meth=method,
               yuqi=assert_result,json=list_json,relusts=listresult)


if __name__ == '__main__':
    unittest.main(verbosity=2)