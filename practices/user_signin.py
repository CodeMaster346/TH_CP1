# TH 2nd User Sign In
user_list = ["Jeffry456", "B3z05!", "Elon6543", "Mu5k!234"]


while True:
    user_input = int(input("1. New User\n2. Returning user\n3. Exit\nType the number of the option you want to choose: "))
    # has user create username and password and appends to list
    if user_input == 1:
        username = input("Create a username: ")
        password = input("Create A password: ")
        print(f"Your username is {username} and your password is {password}")
        user_list.append(username)
        user_list.append(password)
    # asks username and password for returning users
    elif user_input == 2:
        username = input("Input your username: ")
        password = input("Input your password: ")
        username_valid = bool(username in user_list)
        password_valid = bool(password in user_list)
        valid = username_valid and password_valid
        # keeps asking username and password until both are valid
        while password_valid == False:
            print("Invalid username/password")
            password = input("Input your password: ")
            username_valid = bool(username in user_list)
            password_valid = bool(password in user_list)
            valid = username_valid and password_valid
            if valid == True:
                print(f"Welcome back {username}! Have a great day =)")
            else:
                print("Invalid username/password")
    elif user_input == 3:
        print("Bye!")
        raise SystemExit