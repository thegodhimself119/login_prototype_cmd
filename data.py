import secondary
from pymongo import MongoClient
import certifi
import threading
import logged

ca = certifi.where()
client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client["database"]#acess of current databaser
collist = db.list_collection_names()#finding collection list
login = bool()


def create_new():#creation of new collection(account)
    x = str(input(" Enter username for you account "))
    coll = db[x] #acess the collection
    if x in collist:
        print("this account already exists")
    else:

        y = str(input("what will your password be?: "))
        x = str(input("reenter you pw" ))
        if x == y:
            post = {"password": y} #creating a post called password
            coll.insert_one(post) #inserting the post in collection (one at a time)
            print("account sucessfully created!")

        else:
            print("pls try again your password wasnt correct")
            create_new()


def login_after():#login operation
    global pw
    x = str(input(" what is your user name? "))
    col = db[x]#decleration of collection x

    find = col.find({})#find existing collection
    for find in find:
        pw = find["password"]

    if x in collist:  #if it's in collection
        y = str(input(" enter your password for account "))
        if y == pw:   #if pw is correct
            print("you have sucessfully logged in\n\n")
            login = bool(True) #login status
            logged.actions(login) #moved to next file for further
        else:
            print("wrong password")
    else:
        print("this username doesnt exist")

def delete():
      username = input("enter your user name you want to delete ")
      if username in collist:
        col = db[username]
        pw = input("enter your password of your account if you wan't to delete ")
        find = col.find({})
        for find in find:
          pasw= find["password"]
        if pw == pasw:
          col.drop()
          print("account sucessfully deleted")
        else:
          print("wrong password ")
      else:
          print("incorrect username")

def change():
    username = print("what is your username? ")
    col =  db[username]
    if col in collist:
        ques = print("do you want to change password or username? ")
        if ques == "password":
            pass
