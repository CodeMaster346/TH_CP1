# TH 2nd Password Strength Project

uppercaseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowercaseList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numberList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specialList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?"]

while True:
    length = 0
    upper = 0
    lower = 0
    num = 0
    special = 0
    password = input("Input a password: ")
    passwordList = [password]
    if len(password) >= 8:
        length = 1
    
    char_in_upperlist_status = [char in uppercaseList for char in password]
    char_in_lowerlist_status = [char in lowercaseList for char in password]
    char_in_numlist_status = [char in numberList for char in password]
    char_in_speciallist_status = [char in specialList for char in password]

    strength = ((((length + upper) + lower) + num) + special)
    print(f"Strength Score: {strength}/5") 
#     if length is set as 0
#         display you need to make your password longer
#     if upper is set as 0
#         display you need to add an uppercase letter
#     if lower is set as 0
#         display you need to add a lowercase letter
#     if num is set as 0
#         display you need to add a number
#     if special is set as 0
#         display you need to add a special character