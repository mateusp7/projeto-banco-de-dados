import pymongo
import sys
sys.path.append('C:/Apache24/htdocs/projeto-banco-de-dados/projeto-banco-de-dados/')
class MongoConnection:
    def connect(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["beautysalon"]
        self.mycol = self.mydb["users"]
    def close(self):
        self.myclient.close()
        
if __name__ == "__main__":
    MongoConnection.connect()



