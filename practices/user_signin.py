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
        for i in range(len(user_list)):
            # checks if username is in user_list
            if user_list[i] == username:
                valid_password = user_list[i+1]
                password = input("Inout your password: ")
                #checks if the password is with the username
                if password == valid_password:
                    print(f"Welcome back {username}! Have a great day =)")
                else:
                    password_valid = False
                    # keeps asking password until it is valid
                    while password_valid == False:
                        print("Invalid password")
                        password = input("Input your password: ")
                        username_valid = bool(username in user_list)
                        password_valid = bool(password in user_list)
                        valid = username_valid and password_valid
                        if valid == True:
                            print(f"Welcome back {username}! Have a great day =)") 
            else:
                # keeps asking username until it is valid
                while user_list[i] != username:
                    print("Invalid username")
                    password = input("Input your username: ")
                    username_valid = bool(username in user_list)
                    if username_valid == True:
                        print(f"Welcome back {username}! Have a great day =)")
                    else:
                        print("Invalid username")
    elif user_input == 3:
        print("Bye!")
        raise SystemExit