# TH 2nd  Who are you project
userList = []

# for list to update and be used you must keep the code running
while True:
    print("1. Add a new user \n2. Get info from existing user \n3. exit")
    options = int(input("Input the number for the option you want: "))
    if options == 1:
        name = input("What is your name? ")
        age = input("What is your age? ")
        fav_color = input("What is your favorite color? ")
        sentence = f"Hello {name}, your favorite color is {fav_color}, and you are {age}."
        userList.append(name)
        userList.append(sentence)
    elif options == 2:
        user_input = input("What is your name? ")
        for i in range(len(userList)):
            if userList[i] == user_input:
                print(userList[i+1])
    elif options == 3:
        raise SystemExit
    else:
        print("The number you entered was not recognised.")

