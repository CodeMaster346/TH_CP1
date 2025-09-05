#TH 2nd idiot proof

name = input("What is your full name? ").strip().title()
phone = input("Give me your phone number: ")
gpa = input("Give me your GPA: ")

print("--------------------------------------------------------------------------------------")
print(f"Name = {name}")
digits = ''.join(chr for chr in phone if chr.isdigit())
first_three_numbers = digits[:3]
second_three_numbers = digits[3:6]
last_four_numbers = digits[6:10]
print(f"Phone Number = {first_three_numbers} {second_three_numbers} {last_four_numbers}")
print(gpa)
print("--------------------------------------------------------------------------------------")