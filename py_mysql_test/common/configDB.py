__author__ = 'Administrator'
#coding=utf-8
import pymysql,sys
import common.readConfig as Reconfig
import sys
sys.path.insert(1,"..")

localReadingConfig=Reconfig.ReadConfig()

class MyDB():

    def __init__(self,Db):
        # self.log=Log.get_log()
        # self.logger=self.log.get_logger()
        self.db=None
        self.cursor=None
        self.Db=Db
        global host,username,password,port,database,config
        host=localReadingConfig.get_DB(self.Db,'host')
        username=localReadingConfig.get_DB(self.Db,'username')
        password=localReadingConfig.get_DB(self.Db,'password')
        port=localReadingConfig.get_DB(self.Db,'port')
        database=localReadingConfig.get_DB(self.Db,'database')
        config={
            'host':str(host),
            'user':username,
            'password':password,
            'port':int(port),
            'db':database
        }

    def connectDB(self):
        try:
            #connect to DB
            self.db=pymysql.connect(**config)
            # create cursor创建游标对象
            self.cursor=self.db.cursor()
            print('Connect DB successfully!')
        except ConnectionError as ex:
            self.logger.error(str(ex))

    def executeSQL(self,sql,params):
        self.connectDB()
        #executing sql
        self.cursor.execute(sql,params)
        #executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self,cursor):
        value=cursor.fetchall()
        return value

    def get_one(self,cursor):
        value=cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        print("Database closed!")






