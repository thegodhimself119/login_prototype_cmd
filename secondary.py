import data


def login():  # acess from current database
    log = str(input("do you want to login to your account?"))
    logu = log.upper
    if logu == "YES" or "Y":
        data.username()
    else:
        return 0


def main():  # first question for login
    ques = str(input("what operation do you wanna perform?\n-create "
                     "new account\n-login\n"))
    if ques == "create new account":  # creation of data
        data.collection()

    elif ques == "login":
        login()


# start of the program
if __name__ == '__main__':
    main()
