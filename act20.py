from getpass import getpass


login = True

while login == False:
    username = input("enter your username:")
    password = getpass("enter your password:")

    if username == "user123" or password == "user1":
        print("access granted")
        login = True
    else:
        print("access denied")
        