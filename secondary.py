import data

def login():#acess from current database

    data.login_after()

def main():#first question for login
    ques = str(input("what operation do you wanna perform?\n-create "
                     "new account\n-login\n-delete account\n"
                     "-change password/username\n "))
    if ques == "create new account": #creation of data
        data.create_new()

    elif ques == "login":
        login()

    elif ques == "delete account" or ques == "del" or ques == "delete":
        data.delete()

    elif ques == "change password" or ques == "change " or ques == "change username":
        data.change()

#start of the program
if __name__ == '__main__':
    main()

