# TH 2nd Password Strength Project
#CONTAINER for uppercase letters
#CONTAINER for lowercase letters
#CONTAINER for numbers
#CONTAINER for special characters
#CONTAINER for input user passwords
#CONTAINER for password strength scores
#
#LOOP that goes till user decides to exit
#    DISPLAY user choices
#    PROMPT user to input the number of that choices
#    SET user_input AS the input the user gave
#    SET length AS 0
#    SET upper AS 0
#    SET lower AS 0
#    SET num AS 0
#    SET special AS 0
#
#    IF user_choice is set AS 1 THEN
#        PROMPT user to input a password
#        SET password AS the input the user gives
#        IF the length of password is GREATER THAN OR EQUAL TO 8 THEN
#            SET length AS 1
#    
#        REPEAT FOR every character IN password
#            IF character is IN CONATINER for uppercase letters THEN
#                SET upper AS 1
#
#        REPEAT FOR every character IN password
#            IF character is IN CONATINER for lowercase letters THEN
#                SET lower AS 1
#
#        REPEAT FOR every character IN password
#            IF character is IN CONATINER for numbers:
#                SET num AS 1
#
#        REPEAT FOR every character IN password
#            IF character is IN CONATINER for special characters:
#                SET special AS 1
#
#        SET strength AS length PLUS upper PLUS lower PLUS num PLUS special
#        IF strength is EQUAL TO 5 THEN
#            SET password_strength AS Very Strong
#            SET complexity_value AS |||||||||||||||||||||||||
#        ESLE, IF strength is EQUAL TO 4 THEN
#            SET password_strength AS Strong
#            SET complexity_value AS ||||||||||||||||||||-----
#        ELSE, IF strength is EQUAL TO 3 THEN
#            SET password_strength AS Moderate
#            SET complexity_value AS |||||||||||||||----------
#        ELSE, IF strength is EQUAL TO 2 THEN
#            SET password_strength AS Weak
#            SET complexity_value AS ||||||||||---------------
#        ELSE, IF strength is EQUAL TO 1 THEN
#            SET password_strength AS Very Weak
#            SET complexity_value AS |||||--------------------
#        ELSE, if none of these conditions are met THEN
#            SET password_strength AS Password should not exist
#            SER complexity_value AS :(
#    
#        SET strength_score AS strength/5
#        DISPLAY -----------------------------------------------------------------------------------------------------------
#        DISPLAY complexity_value
#                Strength Score: strength_score
#                Password Strength: password_strength
#        DISPLAY -----------------------------------------------------------------------------------------------------------
#        IF length is EQUAL TO 0 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY You need to make your password longer.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        IF upper is EQUAL TO 0 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY You need to add an uppercase letter.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        IF lower is EQUAL TO 0 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY You need to add a lowercase letter.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        IF num is EQUAL TO 0 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY You need to add a number.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        IF special is EQUAL TO 0 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY You need to add a special character.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        ELSE, if none of the above conditions are met THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password needs no changes.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        ADD password to CONATINER for passwords
#        ADD strength_score to CONTAINER for strength scores
#        
#    ELSE, IF user_choice is EQUAL TO 2 THEN
#        SET iteration AS 1
#        DISPLAY -----------------------------------------------------------------------------------------------------------
#        REPEAT FOR every password IN CONTAINER for passwords:
#            DISPLAY {iteration}. {userPasswordList[iteration - 1]}\nStrength Score: {userStrengthScoreList[iteration-1]}
#            SET iteration AS iteration PLUS 1
#        DISPLAY -----------------------------------------------------------------------------------------------------------
#    ELSE, IF user_choice is EQUAL TO 3 THEN
#        DISPLAY -----------------------------------------------------------------------------------------------------------
#        DISPLAY compairson options
#        PROMPT user to give the number of the comparison they want to user
#        SET user_input AS the input the user gives
#        DISPLAY -----------------------------------------------------------------------------------------------------------
#        SET iteration AS 1
#        REPEAT FOR every password IN CONTAINER for passwords:
#            DISPLAY iteration. password
#            SET iteration AS iteration PLUS iteration
#            PROMPT user to input the number of the password
#            SET password_choice AS input the user gives
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        IF user_input is EQUAL TO 1 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY 12345 got a 1/5 because it is easily guessed, only has numbers, and is not 8 characters long.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        ELSE, IF user_input is EQUAL TO 2 THEN
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY 123456789 got a 2/5 because it is easily guessed, and only has numbers, but is over 8 characters long
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        elif user_input == 3:
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY password got a 2/5 because it is easily guessed, and only has lowercase letters, but is 8 characters long.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        elif user_input == 4:
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY admin got a 1/5 because it is easily guessed, only has lowercase letters, and is not 8 characters long.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        elif user_input == 5:
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY 1111111 got a 1/5 because it only has numbers, and is not 8 characters long.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        elif user_input == 6:
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY qwerty got a 1/5 because it only has lowercase letters, and is not 8 characters long.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        elif user_input == 7:
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY asdfgh got a 1/5 because it only has lowercase letters, and is not 8 characters long.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        elif user_input == 8:
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#            DISPLAY Your password got a strength_score
#            DISPLAY FIRSTNAME LASTNAME got a 3/5 but, because it is easily findable, and doesn't have symbols or numbers, it is a very bad password.
#            DISPLAY -----------------------------------------------------------------------------------------------------------
#        else:
#            DISPLAY INVALID INPUT
#    ELSE, IF user_choice is EQUAL TO 4 THEN
#        EXIT the program
#    ELSE, if none of the above conditions are met THEN
#        DISPLAY Invalid Input




#Lists so that you can check if different password requirements apply
uppercaseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercaseList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specialList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]
#Lists for passwords and strength scores
userPasswordList = []
userStrengthScoreList = []

#Keeps code running till user types 4
while True:
    #Lets user choose what option to do
    user_choice = int(input("1. Check password strength\n2. See all passwords entered\n3. Compare to common weak passwords\n4. Exit\nEnter the number for the option you want to choose: "))
    #variables to make making a strength score easier
    length = 0
    upper = 0
    lower = 0
    num = 0
    special = 0

    if user_choice == 1:
        #Has user input a password
        password = input("Input a password: ")
        #checks if password is 8 or more characters long
        if len(password) >= 8:
            length = 1
    
        #Checks if there are uppercase letters in the password
        for char in password:
            if char in uppercaseList:
                upper = 1

        #Checks if there are lowercase letters in the password
        for char in password:
            if char in lowercaseList:
                lower = 1

        #Checks if there are numbers in the password
        for char in password:
            if char in numberList:
                num = 1

        #Checks if there are special characters in the password
        for char in password:
            if char in specialList:
                special = 1

        #Adds values of password requirements and calculates strength
        strength = ((((length + upper) + lower) + num) + special)
        #Creating password strength and complexity outputs using the strength value
        if strength == 5:
            password_strength = "Very Strong"
            complexity_value = "|||||||||||||||||||||||||"
        elif strength == 4:
            password_strength = "Strong"
            complexity_value = "||||||||||||||||||||-----"
        elif strength == 3:
            password_strength = "Moderate"
            complexity_value = "|||||||||||||||----------"
        elif strength == 2:
            password_strength = "Weak"
            complexity_value = "||||||||||---------------"
        elif strength == 1:
            password_strength = "Very Weak"
            complexity_value = "|||||--------------------"
        else:
            password_strength = "Password should not exist"
            complexity_value = ":("

        #Setting the strength score string
        strength_score = f"{strength}/5"
        #Printing out how well they did with password strength
        print("-----------------------------------------------------------------------------------------------------------")
        print(f"[{complexity_value}]\nStrength Score: {strength_score}\nPassword Strength: {password_strength}") 
        print("-----------------------------------------------------------------------------------------------------------")
        # Gives password suggestions if needed
        if length == 0:
            print("-----------------------------------------------------------------------------------------------------------")
            print("You need to make your password longer.")
            print("-----------------------------------------------------------------------------------------------------------")
        if upper == 0:
            print("-----------------------------------------------------------------------------------------------------------")
            print("You need to add an uppercase letter.")
            print("-----------------------------------------------------------------------------------------------------------")
        if lower == 0:
            print("-----------------------------------------------------------------------------------------------------------")
            print("You need to add a lowercase letter.")
            print("-----------------------------------------------------------------------------------------------------------")
        if num == 0:
            print("-----------------------------------------------------------------------------------------------------------")
            print("You need to add a number.")
            print("-----------------------------------------------------------------------------------------------------------")
        if special == 0:
            print("-----------------------------------------------------------------------------------------------------------")
            print("You need to add a special character.")
            print("-----------------------------------------------------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------------------------------------------------")
            print("Your password needs no changes.")
            print("-----------------------------------------------------------------------------------------------------------")
        #puts password and strength score in lists to use later
        userPasswordList.append(password)
        userStrengthScoreList.append(strength_score)
        
    elif user_choice == 2:
        #Prints off all the previous passwords the user made while code has been running
        iteration = 1
        print("-----------------------------------------------------------------------------------------------------------")
        for passwords in userPasswordList:
            print(f"{iteration}. {userPasswordList[iteration - 1]}\nStrength Score: {userStrengthScoreList[iteration-1]}")
            iteration += 1
        print("-----------------------------------------------------------------------------------------------------------")
    elif user_choice == 3:
        # Gives user options to compare one of their passwords to
        print("-----------------------------------------------------------------------------------------------------------")
        user_input = int(input("1. 12345\n2. 123456789\n3. password\n4. admin\n5. 1111111\n6. qwerty\n7. asdfgh\n8. FIRSTNAME LASTNAME\nChoose the number of the password you want to compare one of your passwords to: "))
        print("-----------------------------------------------------------------------------------------------------------")
        iteration = 1
        print("-----------------------------------------------------------------------------------------------------------")
        #Prints off passwords and lets user choose which to compare to their first option
        for passwords in userPasswordList:
            print(f"{iteration}. {userPasswordList[iteration - 1]}")
            iteration += 1
            
        password_choice = int(input("Input the number of the password you want to compare the weak password to: "))
        print("-----------------------------------------------------------------------------------------------------------")
        #Tells user their strength score and tells user the comparisons strength score and why the password is bad
        if user_input == 1:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("12345 got a 1/5 because it is easily guessed, only has numbers, and is not 8 characters long.")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 2:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("123456789 got a 2/5 because it is easily guessed, and only has numbers, but is over 8 characters long")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 3:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("password got a 2/5 because it is easily guessed, and only has lowercase letters, but is 8 characters long.")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 4:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("admin got a 1/5 because it is easily guessed, only has lowercase letters, and is not 8 characters long.")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 5:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("1111111 got a 1/5 because it only has numbers, and is not 8 characters long.")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 6:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("qwerty got a 1/5 because it only has lowercase letters, and is not 8 characters long.")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 7:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("asdfgh got a 1/5 because it only has lowercase letters, and is not 8 characters long.")
            print("-----------------------------------------------------------------------------------------------------------")
        elif user_input == 8:
            print("-----------------------------------------------------------------------------------------------------------")
            print(f"Your password got a {userStrengthScoreList[password_choice - 1]}")
            print("FIRSTNAME LASTNAME got a 3/5 but, because it is easily findable, and doesn't have symbols or numbers, it \nis a very bad password.")
            print("-----------------------------------------------------------------------------------------------------------")
        else:
            print("Invalid Input")
    elif user_choice == 4:
        #Makes the program stop running
        raise SystemExit
    else:
        print("Invalid Input")
