#TH 2nd idiot proof
        
while True:
    first_name = input("What is your first name? ").strip().title()
    last_name = input("What is your last name? ").strip().title()
    phone = input("Give me your phone number: ")
    gpa = float(input("Give me your GPA: "))
    if gpa > 4 or gpa < 0:
        print("--------------------------------------")
        print("Are you stupid? Input a GPA number!")
        print("--------------------------------------")
    elif first_name.isalpha() or last_name.isalpha() == False:
        print("--------------------------------------")
        print("Are you stupid? Input a name!")
        print("--------------------------------------")
    else:
        print("--------------------------------------------------------------------------------------")
        print(f"Name = {name}")
        digits = ''.join(chr for chr in phone if chr.isdigit())
        first_three_numbers = digits[:3]
        second_three_numbers = digits[3:6]
        last_four_numbers = digits[6:10]
        print(f"Phone Number = {first_three_numbers} {second_three_numbers} {last_four_numbers}")
        print(round(gpa, 1))
        print("--------------------------------------------------------------------------------------")