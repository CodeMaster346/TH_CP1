#TH 2nd Combat Program
import random as rand
monsterList = ["Bear","Hydra","Dragon","Zombie","Wild Fox","American","Giant Golden Eagle","Programmer","Tesla","Skully from Waltz of the Wizard","Steve","The Great Hog","Casual Citezen"]
monsterHealthList = [10]
monsterDefnenseList = [20]

print("Welcome User! Before we start, I just need some info from you.")
user_name = input("What is you name? ")
fighter_class = int(input("1. Fighter\n2. Mage\n3. Rouge\nInput the number of the fighter class you are"))

if fighter_class == 1:
    fighter_class = "Fighter"
    hp = 30
    defense = 20
    print("Great, here are your stats")
    print(f"HP = {hp}\nDefense = {defense}\nAttack = D20 + 3\nDamage = D8 + 4")
elif fighter_class == 2:
    fighter_class = "Mage"
    hp = 40
    defense = 35
    print("Great, here are your stats")
    print(f"HP = {hp}\nDefense = {defense}\nAttack = D20 + 3\nDamage = D8 + 4")
elif fighter_class == 3:
    fighter_class = "Rouge"
    hp = 45
    defense = 10
    print("Great, here are your stats")
    print(f"HP = {hp}\nDefense = {defense}\nAttack = D20 + 3\nDamage = D8 + 4")


