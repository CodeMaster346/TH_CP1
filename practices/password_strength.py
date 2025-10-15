# TH 2nd Password Strength Project

uppercaseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercaseList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specialList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]
userPasswordList = []
userStrengthScoreList = []

while True:
    user_choice = int(input("1. Check password strength\n2. See all passwords entered\n3. Compare to common weak passwords\n4. Exit\nEnter the number for the option you want to choose: "))
    length = 0
    upper = 0
    lower = 0
    num = 0
    special = 0

    if user_choice == 1:
        password = input("Input a password: ")
        if len(password) >= 8:
            length = 1
    
        for char in password:
            if char in uppercaseList:
                upper = 1

        for char in password:
            if char in lowercaseList:
                lower = 1

        for char in password:
            if char in numberList:
                num = 1

        for char in password:
            if char in specialList:
                special = 1

    
        strength = ((((length + upper) + lower) + num) + special)
        if strength == 5:
            password_strength = "Very Strong"
        elif strength == 4:
            password_strength = "Strong"
        elif strength == 3:
            password_strength = "Moderate"
        elif strength == 2:
            password_strength = "Weak"
        elif strength == 1:
            password_strength = "Very Weak"
        else:
            password_strength = "Password should not exist"

        if strength == 5:
            complexity_value = "|||||||||||||||||||||||||"
        elif strength == 4:
            complexity_value = "||||||||||||||||||||-----"
        elif strength == 3:
            complexity_value = "|||||||||||||||----------"
        elif strength == 2:
            complexity_value = "||||||||||---------------"
        elif strength == 1:
            complexity_value = "|||||--------------------"
        else:
            complexity_value = ":("
    
        strength_score = f"{strength}/5"
        print("-----------------------------------------------------------------------------------------------------------")
        print(f"[{complexity_value}]\nStrength Score: {strength_score}\nPassword Strength: {password_strength}") 
        print("-----------------------------------------------------------------------------------------------------------")
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
        elif strength == 5:
            print("-----------------------------------------------------------------------------------------------------------")
            print("Your password needs no changes.")
            print("-----------------------------------------------------------------------------------------------------------")
        userPasswordList.append(password)
        userStrengthScoreList.append(strength_score)
        
    elif user_choice == 2:
        iteration = 1
        print("-----------------------------------------------------------------------------------------------------------")
        for passwords in userPasswordList:
            print(f"{iteration}. {userPasswordList[iteration - 1]}\nStrength Score: {userStrengthScoreList[iteration-1]}")
            iteration += 1
        print("-----------------------------------------------------------------------------------------------------------")
    elif user_choice == 3:
        user_input = int(input("1. 12345\n2. 123456789\n3. password\n4. admin\n5. 1111111\n6. qwerty\n7. asdfgh\n8. FIRSTNAME LASTNAME\n9. PETS NAME\n10. MM/DD/YYYY\n11. PHONE NUMBER"))