import os,configHttp
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree
from common.Log import MyLog as Log

localConfigHttp = configHttp.ConfigHttp()
log=Log.get_log()
logger=log.get_logger()

#从excel文件中读取测试用例
def get_xls(xls_name,sheet_name):
    cls=[]
    #get xls file's path
    xlsPath=os.path.join(proDir,'testFile',xls_name)
    #open xls file
    file=open_workbook(xlsPath)
    #get sheet by name
    sheet=file.sheet_by_name(sheet_name)


