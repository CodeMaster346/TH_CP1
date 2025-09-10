# TH 2nd Random Numbers Notes

import random

# examples of random numbers
print(random.random()) # float between 0 and 1

print(random.randint(5, 800))

name = input("What is your name? ").strip().title()

# random DND stat creator
stat_one = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
stat_two = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
stat_three = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
stat_four = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
stat_five = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
stat_six = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
stat_seven = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10)
print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

strength = int(input("Which stat are you making your strength? "))
charisma = int(input("Which stat are you making your charisma? "))
dexterity = int(input("Which stat are you making your dexterity? "))
wisdom = int(input("Which stat are you making your wisdom? "))
intellegence = int(input("Which stat are you making your intellegence? "))
constitution = int(input("Which stat are you making your constitution? "))