'''
create on 2017-07-20
author kevin
Python中的staticmethod主要是方便将外部函数集成到类体中，在不需要类实例化的情况下调用方法
pthon 静态方法
'''

#1.不使用staticmethod

'''
IND='ON'
def checkind():
    return (IND=='ON')

class Kls(object):
    def __init__(self,data):
        self.data=data

    def do_reset(self):
        if checkind():
            print('reset done for:',self.data)
        else:
            print('IND is not equal ON')

    def set_db(self):
        if checkind():
            self.db='New db connection'
            print('DB connection made for:',self.data)
        else:
            print('IND is not equal ON too')

ik1=Kls(12)
ik1.do_reset()
ik1.set_db()
'''

#2.使用staticmethod，使用staticmethod包装的方法可以内部调用，也可以通过类访问或类实例化访问
IND='ON'
class Kls(object):
    def __init__(self,data):
        self.data=data

    @staticmethod
    def checkind():
        return (IND=='ON')

    def do_reset(self):
        if self.checkind():
            print('Reset done for:',self.data)
        else:
            print('IND is not equal ON')

    def set_db(self):
        if self.checkind():
            self.db='New db connection'
            print('DB connection made for:',self.data)
        else:
            print('IND is not equal ON too')

ik1=Kls(24)
ik1.do_reset()
ik1.set_db()

print(ik1.checkind()) #实例化访问
print(Kls.checkind()) #类访问

