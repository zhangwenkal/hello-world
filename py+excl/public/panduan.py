__author__ = 'Administrator'
# encoding: utf-8
from  public.log import LogHelper
import operator

log=LogHelper('断言测试结果').add_loger()
'''
def assert_in(asserqiwang,fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(fanhuijson[key])) for key in result.keys()])
        value2=([(str(value)) for value in result.values()])
        if value1==value2:
            return  'pass'
        else:
            return 'fail'
    else:
        LOG.info('填写测试预期值')
        raise ('请填写期望值')
@logger('断言测试结果')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('填写测试预期值')
        raise ('请填写期望值')
'''

def assert_in(fanhuijson,assertqiwang):
    try:
        if operator.eq(fanhuijson,assertqiwang):
            return 'pass'
        else:
            return 'fail'
    except:
        log.info('填写测试期望值:%s'%(str(Exception)))
        raise ('请填写期望值')


