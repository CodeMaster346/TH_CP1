#TH 2nd Combat Program
import time
import random as rand
monsterList = ["a Bear","a Hydra","a Dragon","a Zombie","a Wild Fox","an American","a Giant Golden Eagle","a Programmer","a Tesla","Skully from Waltz of the Wizard","Steve","The Great Hog","a Casual Citezen"]
monsterHealthList = [10, 200, 40, 5, 3, 10, 50, 500, 0.5, 4, 20, 200, 5]
monsterDefnenseList = [3, 20, 20, 1, 2, 20, 20, 20, 0.3, 20, 6, 20, 4]

def monster_turn(hp, defense):
    print("===============================")
    print("The monster is attacking you!")
    print("===============================")
    time.sleep(2)
    monster_attack_roll = rand.randint(1, 20) + rand.randint(1, 20)
    print("===============================")
    print(f"The monster rolled a {monster_attack_roll} to attack!")
    print("===============================")
    time.sleep(2)
    if monster_attack_roll > defense:
        print("===============================")
        print("The monster hit you!")
        print("===============================")
        time.sleep(2)
        monster_damage_roll = rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8)
        print("===============================")
        print(f"The monster rolled a {monster_damage_roll} for damage!")
        print("===============================")
        time.sleep(2)
        hp -= monster_damage_roll
        if hp <= 0:
            hp = 0
        else:
            hp = hp
        print("===============================")
        print(f"You now have {hp} HP left.")
        print("===============================")
        time.sleep(2)
    else:
        print("===============================")
        print("The monster missed!")
        print("===============================")
    time.sleep(2)
    return hp

def user_turn(hp, monster_defense, health_potions):
    print("=========================================")
    attack_type = int(input("1. Normal Attack\n2. Wild Attack(can double damage but damages yourself as well)\n3. Drink Health Potion(Heals 10 HP)\n4. Flee(may or may not actually work)\nInput the number of the option you want to choose: "))
    print("=========================================")
    if attack_type == 1:
        print("===============================")
        print("You chose Normal Attack!")
        print("===============================")
        time.sleep(2)
        if fighter_class == "Fighter":
            attack_roll = rand.randint(1, 20) + rand.randint(1, 20) + 3
            print("===============================")
            print(f"You rolled a {attack_roll} to attack!")
            print("===============================")
        elif fighter_class == "Mage":
            attack_roll = rand.randint(1, 20) + rand.randint(1, 20) - 1
            print("===============================")
            print(f"You rolled a {attack_roll} to attack!")
            print("===============================")
        else:
            attack_roll = rand.randint(1, 20) + rand.randint(1, 20)
            print("===============================")
            print(f"You rolled a {attack_roll} to attack!")
            print("===============================")
        time.sleep(2)
        if attack_roll > monster_defense:
            print("===============================")
            print("You hit the monster!")
            print("===============================")
            time.sleep(2)
            if fighter_class == "Fighter":
                damage_roll = rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8) + 4
                print("===============================")
                print(f"You rolled a {damage_roll} for damage!")
                print("===============================")
            elif fighter_class == "Mage":
                damage_roll = rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8) + 6
                print("===============================")
                print(f"You rolled a {damage_roll} for damage!")
                print("===============================")
            else:
                damage_roll = rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8) + 10
                print("===============================")
                print(f"You rolled a {damage_roll} for damage!")
                print("===============================")
            time.sleep(2)
            monsterHealthList[monster_and_stats] -= damage_roll
            if monsterHealthList[monster_and_stats] <= 0:
                monsterHealthList[monster_and_stats] = 0
            else:
                monsterHealthList[monster_and_stats] = monsterHealthList[monster_and_stats]
            print("===============================")
            print(f"The monster now has {monsterHealthList[monster_and_stats]}\nHP left.")
            print("===============================")
            time.sleep(2)
        else:
            print("===============================")
            print("You missed!")
            print("===============================")
        time.sleep(2)
    elif attack_type == 2:
        print("===============================")
        print("You chose Wild Attack!")
        print("===============================")
        time.sleep(2)
        if fighter_class == "Fighter":
            attack_roll = rand.randint(1, 20) + rand.randint(1, 20) + 3
            print(f"You rolled a {attack_roll} to attack!")
        elif fighter_class == "Mage":
            attack_roll = rand.randint(1, 20) + rand.randint(1, 20) - 1
            print(f"You rolled a {attack_roll} to attack!")
        else:
            attack_roll = rand.randint(1, 20) + rand.randint(1, 20)
            print(f"You rolled a {attack_roll} to attack!")
        time.sleep(2)
        if attack_roll > monster_defense:
            print("===============================")
            print("You hit the monster!")
            print("===============================")
            time.sleep(2)
            if fighter_class == "Fighter":
                damage_roll = (rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8) + 4) * 2
                print("===============================")
                print(f"You rolled a {damage_roll} for damage!")
                print("===============================")
            elif fighter_class == "Mage":
                damage_roll = (rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8) + 6) * 2
                print("===============================")
                print(f"You rolled a {damage_roll} for damage!")
                print("===============================")
            else:
                damage_roll = (rand.randint(1, 8) + rand.randint(1, 8) + rand.randint(1, 8) + 10) * 2
                print("===============================")
                print(f"You rolled a {damage_roll} for damage!")
                print("===============================")
            time.sleep(2)
            monsterHealthList[monster_and_stats] -= damage_roll
            if monsterHealthList[monster_and_stats] <= 0:
                monsterHealthList[monster_and_stats] = 0
            else:
                monsterHealthList[monster_and_stats] = monsterHealthList[monster_and_stats]
            print("===============================")
            print(f"The monster now has {monsterHealthList[monster_and_stats]}\nHP left.")
            print("===============================")
            time.sleep(2)
            self_damage = rand.randint(1, 6)
            hp -= self_damage
            print("===============================")
            print(f"You hurt yourself in the \nprocess and lost {self_damage} HP!\nYou now have {hp} HP left.")
            print("===============================")
            time.sleep(2)
        else:
            print("===============================")
            print("You missed!")
            print("===============================")
    elif attack_type == 3:
        health_potions -= 1
        if health_potions < 0:
            print("===============================")
            print("You dont have any health\npotions to drink!")
            print("===============================")
            time.sleep(2)
        else:
            print("===============================")
            print(f"You chose to Drink a Health\npotion and regained 10 HP.\nYou now have {health_potions}\nhealth potions left.")
            print("===============================")
            time.sleep(2)
            hp += 10
            print("===============================")
            print(f"You now have {hp} HP.")
            print("===============================")
            time.sleep(2)
    elif attack_type == 4:
        can_flee = rand.randint(1, 2)
        if can_flee == 1:
            print("===============================")
            print("You successfully fleed the battle!")
            print("===============================")
            raise SystemExit
        else:
            print("===============================")
            print("You were not able to flee and took 4 damage.")
            print("===============================")
            hp -= 4
            time.sleep(2)
    else:
        print("===============================")
        print("You did not choose a valid option.\nYou lose your turn. Sorry!")
        print("===============================")
        time.sleep(2)
    return hp
    return health_potions

print("Welcome User! Before we start, I just need some info from you.")
user_name = input("What is you name? ")
print("=========================================")
fighter_class = int(input("1. Fighter\n2. Mage\n3. Rouge\nInput the number of the fighter class you are: "))
print("=========================================")
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
    defense = 20
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
monster_health = monsterHealthList[monster_and_stats]
monster_defense = monsterDefnenseList[monster_and_stats]
time.sleep(5)
first_attack = rand.randint(1, 2)
if first_attack == 1:
    print("===============================")
    print("You attack first!")
    print("===============================")
    health_potions = 5
    while hp > 0 and monsterHealthList[monster_and_stats] > 0:
        health_potions = health_potions
        user_turn(hp, monster_defense, health_potions)
        if monsterHealthList[monster_and_stats] <= 0:
            print("===============================")
            print(f"{monsterList[monster_and_stats]} has been defeated!\n{user_name} wins!")
            print("===============================")
        else:
            monster_turn(hp, defense)
            if hp <= 0:
                print("===============================")
                print(f"{user_name} has been defeated.\n{monsterList[monster_and_stats]} wins!")
                print("===============================")
else:
    print("===============================")
    print("The monster attacks first!")
    print("===============================")
    health_potions = 5
    while hp > 0 and monsterHealthList[monster_and_stats] > 0:
        monster_turn(hp, defense)
        if hp <= 0:
            print("===============================")
            print(f"{user_name} has been defeated.\n{monsterList[monster_and_stats]} wins!")
            print("===============================")
        else:
            
            user_turn(hp, monster_defense)
            if monsterHealthList[monster_and_stats] <= 0:
                print("===============================")
                print(f"{monsterList[monster_and_stats]} has been defeated!\n{user_name} wins!")
                print("===============================")
        
