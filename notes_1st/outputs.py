# TH 2nd Format Outputs Notes

name = "Jake"
age = 21
grade = .75
money = 25
print(f"Hello {name}, nice to meet you!\nYou are {age:b}. That is really old!\nYou have a {grade:%} in the class!\nYou have ${money:.2f}, that is a lot of money!")
print("Hello {}, nice to meet you! You are {:b}. That is really old! You have a {:%} in the class! You have ${:.2f}, that is a lot of money!".format(name, age, grade, money))