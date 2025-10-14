# TH 2nd Password Strength Project

uppercaseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercaseList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specialList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]
userPasswordList = []
strengthScoreList = []

while True:
    user_choice = input("1. Check password strength\n2. ")
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

        print(f"[{complexity_value}]\nStrength Score: {strength_score}\nPassword Strength: {password_strength}") 

        if length == 0:
            print("You need to make your password longer.")
        if upper == 0:
            print("You need to add an uppercase letter.")
        if lower == 0:
            print("You need to add a lowercase letter.")
        if num == 0:
            print("You need to add a number.")
        if special == 0:
            print("You need to add a special character.")
        elif strength == 5:
            print("Your password needs no changes.")
        userPasswordList.append(password)
        strengthScoreList.append()
        
    elif user_choice == 2:
