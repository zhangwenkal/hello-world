__author__ = 'Administrator'
import readConfig as Reconfig
from xml.etree import ElementTree as ElementTree
import os

localReadingConfig=Reconfig.ReadConfig()
proDir=Reconfig.pro

#read sql xml
database={}

def set_xml():
    '''
    set sql xml
    :return:
    '''
    if len(database)==0:
        sql_path=os.path.join(proDir,"testFile",'SQL.xml')
        tree=ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name=db.get("name")
            #print(db_name)
            table={}
            for tb in db.getchildren():
                table_name=tb.get("name")
                #print(table_name)
                sql={}
                for data in tb.getchildren():
                    sql_id=data.get("id")
                    #print(sql_id)
                    sql[sql_id]=data.text
                table[table_name]=sql
            database[db_name]=table

def get_xml_dict(database_name,table_name):
    '''
    get db dict by given name
    :param database_name:
    :param table_name:
    :return:
    '''
    set_xml()
    database_dict=database.get(database_name).get(table_name)
    return database_dict

def get_sql(database_name,table_name,sql_id):
    '''

    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    '''

    db=get_xml_dict(database_name,table_name)
    sql=db.get(sql_id)
    return sql

























