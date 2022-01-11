from pymongo import MongoClient
import certifi
import threading
import logged
#used to display database
ca = certifi.where()
client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["database"]#acess of current databaser
collist = db.list_collection_names()#finding collection list



for collist in collist:
    col = db[collist]
    dis = col.find_one({},{"_id":0} )
    print("username:(",collist,")  ",dis)