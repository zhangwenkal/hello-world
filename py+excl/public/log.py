#coding=utf-8
import logging,time,os
from public.path import get_super_path

LOG_PATH=get_super_path()+'\log\log_'

class LogHelper():
    def __init__(self,logger_name):
        self.logger_name=logger_name
        self.info_path=''.join([LOG_PATH,'info.log'])
        self.error_parh=''.join([LOG_PATH,"error.log"])

    def add_loger(self):
        """
        设置log输出级别，格式：
        :return:
        """
        logger=logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            logger_info=logging.FileHandler(self.info_path)
            logger_info.setLevel(logging.INFO)
            logger_error=logging.FileHandler(self.error_parh)
            logger_error.setLevel(logging.ERROR)
            fmt ="%(asctime)s=>[%(name)s - %(levelname)s]:%(message)s"
            fmt_data =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            formatter=logging.Formatter(fmt,fmt_data)
            logger_info.setFormatter(formatter)
            logger_error.setFormatter(formatter)
            logger.addHandler(logger_info)
            logger.addHandler(logger_error)

        return logger

if __name__ == '__main__':
    log=LogHelper('login11').add_loger()
    log.info('info_data')
    log.error('error_data')
