import secondary
from pymongo import MongoClient
import certifi
import threading
import logged

ca = certifi.where()
client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["database"]  # acess of current databaser
collist = db.list_collection_names()  # finding collection list
login = bool()


def collection():  # creation of new collection(account)
    x = str(input(" Enter username for you account "))
    coll = db[x]  # acess the collection
    if x in collist:
        print("this account already exists")
    else:

        y = str(input("what will your password be?: "))
        post = {"password": y}  # creating a post called password
        coll.insert_one(post)  # inserting the post in collection (one at a time)
    print("account successfully created!")


def username():  # login operation
    global pw
    x = str(input(" what is your user name? "))
    col = db[x]  # declaration of collection x

    find = col.find({})  # find existing collection
    for find in find:
        pw = find["password"]

    if x in collist:  # if it's in collection
        y = str(input(" enter your password for account "))
        if y == pw:  # if pw is correct
            print("you have successfully logged in")
            login = bool(True)  # login status
            logged.actions(login)  # moved to next file for further
        else:
            print("wrong password")
    else:
        print("this username doesnt exist")
