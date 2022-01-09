def actions(login):
    while login == True:
        print("welcome to the world you have sucessfully logged in!")
        a = str(input("do you want to still be logged in or logged out yes/no \n Y/N: "))
        ans = a.upper()
        if ans == "YES" or ans == "Y":
           print("hello")
           break
        else:
            break

