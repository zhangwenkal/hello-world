__author__ = 'Administrator'
import os
import readConfig as Reconfig
import logging
from datetime import datetime
import threading

localReadingConfig=Reconfig.ReadConfig()

class Log():
    def __init__(self):
        global logPath,resultPath,ProDir
        proDir=Reconfig.pro
        resultPath=os.path.join(proDir,"result")
        if not os.path.exists(resultPath):
           os.mkdir(resultPath)
        logPath=os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%s")))
        if not  os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger=logging.getLogger()
        #设置日志级别
        self.logger.setLevel(logging.INFO)

        #define handler
        handler=logging.FileHandler(os.path.join(logPath,"output.log"))
        #define  formatter
        formatter=logging.Formatter("%(asctime)s——%(name)s——%(levelname)s——%(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        '''
        get logger
        :return:
        '''
        return self.logger

    def build_start_line(self,case_no):
        '''
        write start line
        :param case_no:
        :return:
        '''
        self.logger.info("------" + case_no + "START------")

    def build_end_line(self,case_no):
        '''
        write  end  line
        :param case_no:
        :return:
        '''
        self.logger.info("------" + case_no + "END------")



