__author__ = 'Administrator'
#coding=utf-8
import os
import codecs
import configparser

#获取当前目录
# proDir=os.path.split(os.path.realpath(__file__))[0]
# print(os.getcwd())
#获取上级目录
#print (os.path.dirname(os.getcwd()))
pro=os.path.split(os.path.realpath(__file__))[0]
pro=os.path.abspath(os.path.join(pro,".."))
configPath=os.path.join(pro,'config')

class ReadConfig():
    def __init__(self):
        with open(configPath,'r') as f:
            data=f.read()
            #remove BOM
            if data[:3]==codecs.BOM_UTF8:
                data=data[3:]
                with  codecs.open(configPath,'w') as fi:
                    fi.write(data)
        #初始化实例
        self.cf=configparser.ConfigParser()
        #读取配置文件
        self.cf.read(configPath)

    def get_DB(self,section_name,name):
        value=self.cf.get(section_name,name)
        return value

# if __name__ == '__main__':
#     Re=ReadConfig()


