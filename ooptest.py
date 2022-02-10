from pymongo import MongoClient
import certifi



class consts:
    ca = certifi.where()
    client = MongoClient("mongodb+srv://yubik:12345@cluster0.cklcq.mongodb.net/?retryWrites=true&w=majority",
                         tlsCAFile=ca)
    db = client["database"]  # acess of current databaser
    collist = db.list_collection_names()  # finding collection list
    login = bool()


class operations:

    def create_new(self):
        x = str(input(" Enter username for you account "))
        coll = consts.db[x]  # acess the collection
        if x in consts.collist:
            print("this account already exists")
        else:

            y = str(input("what will your password be?: "))
            x = str(input("reenter you pw"))
            if x == y:
                post = {"password": y}  # creating a post called password
                coll.insert_one(post)  # inserting the post in collection (one at a time)
                print("account sucessfully created!")

            else:
                print("pls try again your password wasnt correct")
                operations.create_new()

    def login_after(self):
        x = str(input(" what is your user name? "))
        col = consts.db[x]  # decleration of collection x

        find = col.find({})  # find existing collection
        for find in find:
            pw = find["password"]

        if x in consts.collist:  # if it's in collection
            y = str(input(" enter your password for account "))
            if y == pw:  # if pw is correct
                print("you have sucessfully logged in\n\n")
                login = bool(True)  # login status
                # moved to next file for further
            else:
                print("wrong password")
        else:
            print("this username doesnt exist")

    def delete(self):
        username = input("enter your user name you want to delete ")
        if username in consts.collist:
            col = consts.db[username]
            pw = input("enter your password of your account if you wan't to delete ")
            find = col.find({})
            for find in find:
                pasw = find["password"]
            if pw == pasw:
                col.drop()
                print("account sucessfully deleted")
            else:
                print("wrong password ")
        else:
            print("incorrect username")


class logic:

    def start(self):
        ques = str(input("what operation do you wanna perform?\n-create "
                         "new account\n-login\n-delete account\n"
                         "-change password/username\n "))
        if ques == "create new account":  # creation of data

            o.create_new()

        elif ques == "login":
            o.login_after()

        elif ques == "delete account" or ques == "del" or ques == "delete":
            o.delete()

        elif ques == "change password" or ques == "change " or ques == "change username":
            pass

class queries:

    def mongo(self):
        for collist in consts.collist:
            col = consts.db[collist]
            find = col.find({})  # find existing collection
            for find in find:
                pw = find["password"]
                print("username:", collist, "// password: ", pw)



query = queries()
o = operations()
log = logic()
def main():
    ques = input("do you want to run query or execute?\n")
    if ques == "query":
        query.mongo()

    if ques == "execute":
        log.start()

if __name__ == '__main__':
    main()




