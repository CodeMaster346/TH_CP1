#TH 2nd Final Project
import time
import random

powerUpOptions = ["Health Potions", "Strength Potions", "Extra Armor", "Sword", "Bow and Arrow", "Wizard staff", "Firebending Potion", "Speed Potion"]
statDictionary = {"Player Health" : 30, "Player Damage" : 5, "Guard Health" : 40, "Guard Damage" : 8, "Witch Health" : 35, "Witch Damage" : 10}
powerUps = ["0", "Speed Potion"]

def restart():
    restarting_choice = input("Do you wish to restart(Y/N): ")
    restarting_choice = restarting_choice.upper()
    if restarting_choice == "Y":
        print("Restarting...")
        time.sleep(5)
    elif restarting_choice == "N":
        raise SystemExit
    else:
        while restarting_choice != "Y" and "N":
            print("Invalid Input")
            restarting_choice = input("Do you wish to restart(Y/N): ")
            restarting_choice.upper()

def win_or_lose(check_win, win_sentence):
    if check_win == True:
        print(win_sentence)
        power_up_1 = powerUpOptions[random.randint(1, 8) - 1]
        power_up_2 = powerUpOptions[random.randint(1, 8) - 1]
        power_up_3 = powerUpOptions[random.randint(1, 8) - 1]
        powerUps.append(power_up_1)
        powerUps.append(power_up_2)
        powerUps.append(power_up_3)
    else:
        print("You Lost")
        restart()

def battle(monster):
    print(f"You Are battling the {monster}\nIts stats are:\nHealth = {statDictionary[f"{monster} Health"]}\nDamage = {statDictionary[f"{monster} Damage"]}")
    while statDictionary[f"{monster} Health"] > 0 and statDictionary[f"Player Health"] > 0:
        print("It is your turn!")
        print(f"Your stats are:\nHealth = {statDictionary['Player Health']}\nDamage = {statDictionary['Player Damage']}")
        battle_choice = input("1. Regular\n2. Use Power-up\n3. Wild attack(Double damage but causes damage to you as well)\n4. Attempt to run\nInput the number of the option you wish to choose: ")
        num = battle_choice.isdigit()
        if num == True:
            battle_choice = int(battle_choice)
        else:
            while num == False:
                print("Invalid Input")
                battle_choice = input("1. Regular\n2. Use Power-up\n3. Wild attack(Double damage but causes damage to you as well)\n4. Attempt to run\nInput the number of the option you wish to choose: ")
                num = battle_choice.isdigit()
                if num == True:
                    battle_choice = int(battle_choice)

        hit = random.randint(1, 2)
        if battle_choice == 1:
            hit = random.randint(1, 2)
            if hit == 1:
                print(f"It was a hit! The {monster} lost {statDictionary['Player Damage']} health.")
                statDictionary[f"{monster} Health"] -= statDictionary["Player Damage"]
                print(statDictionary[f"{monster} Health"])
            else:
                print("You missed!")
        elif battle_choice == 2:
            if powerUps[0] in powerUpOptions:
                iteration = 0
                for i in powerUpOptions:
                    print(f"{iteration + 1}. {i}")
                    iteration += 1
                power_up_choice = input("Input the name of the power-up you want to use: ")
                power_up_choice.capitalize()
                if power_up_choice in powerUps:
                    if power_up_choice == powerUpOptions[0]:
                        statDictionary["Player Health"] += 10
                    if power_up_choice == powerUpOptions[1]:
                        statDictionary["Player Health"] += 10
                    if power_up_choice == powerUpOptions[2]:
                        statDictionary["Player Health"] += 10
                    if power_up_choice == powerUpOptions[3]:
                        statDictionary["Player Health"] += 10
                    if power_up_choice == powerUpOptions[4]:
                        statDictionary["Player Health"] += 10
                    if power_up_choice == powerUpOptions[5]:
                        statDictionary["Player Health"] += 10
                    if power_up_choice == powerUpOptions[6]:
                        statDictionary["Player Health"] += 10
                    else:
                        escape = True
                        powerUps.__delitem__["Speed Potion"]

        elif battle_choice == 3:
            hit = random.randint(1, 2)
            if hit == 1:
                print(f"It was a hit! The {monster} lost {statDictionary['Player Damage']} health.")
                statDictionary[f"{monster} Health"] -= statDictionary["Player Damage"]
                print(statDictionary[f"{monster} Health"])
            else:
                print("You missed!")
            

battle("Guard")
    
