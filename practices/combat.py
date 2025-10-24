#TH 2nd Combat Program
import time
import random as rand
monsterList = ["a Bear","a Hydra","a Dragon","a Zombie","a Wild Fox","an American","a Giant Golden Eagle","a Programmer","a Tesla","Skully from Waltz of the Wizard","Steve","The Great Hog","a Casual Citezen"]
monsterHealthList = [10, 200, 40, 5, 3, 10, 50, 500, 0.5, 4, 20, 200, 5]
monsterDefnenseList = [3, 30, 35, 1, 2, 30, 35, 35, 0.3, 35, 6, 20, 4]

print("Welcome User! Before we start, I just need some info from you.")
user_name = input("What is you name? ")
print("=========================================")
fighter_class = int(input("1. Fighter\n2. Mage\n3. Rouge\nInput the number of the fighter class you are: "))

if fighter_class == 1:
    fighter_class = "Fighter"
    hp = 30
    defense = 20
    print("=========================================")
    print("Great, here are your stats")
    print(f"HP = {hp}\nDefense = {defense}\nAttack = 2D20 + 3\nDamage = 3D8 + 4")
    print("=========================================")
    time.sleep(5)
elif fighter_class == 2:
    fighter_class = "Mage"
    hp = 40
    defense = 35
    print("=========================================")
    print("Great, here are your stats")
    print(f"HP = {hp}\nDefense = {defense}\nAttack = 2D20 - 1\nDamage = 3D8 + 6")
    print("=========================================")
    time.sleep(5)
else:
    fighter_class = "Rouge"
    hp = 45
    defense = 10
    print("=========================================")
    print("Great, here are your stats")
    print(f"HP = {hp}\nDefense = {defense}\nAttack = 2D20\nDamage = 3D8 + 10")
    print("=========================================")
    time.sleep(5)

monster_and_stats = rand.randint(0,12)
print("=========================================")
print(f"You come across {monsterList[monster_and_stats]}\nIts stats are:\nHP = {monsterHealthList[monster_and_stats]}\nDefense = {monsterDefnenseList[monster_and_stats]}")
print("=========================================")