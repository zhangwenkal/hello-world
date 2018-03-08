__author__ = 'Administrator'
from common.configDB import MyDB
import sys
sys.path.insert(1,"..")

class park_user(MyDB):
    def connect(self):
        self.connectDB()


#MyDB('DATABASE1').connectDB()

if __name__ == '__main__':
    park_user("DATABASE1").connectDB()