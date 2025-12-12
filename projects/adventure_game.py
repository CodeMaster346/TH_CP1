#TH 2nd Final Project
import time
import random

escape = False

powerUpOptions = ["Health Potions", "Strength Potions", "Extra Armor", "Sword", "Bow and Arrow", "Wizard staff", "Firebending Potion", "Speed Potion"]
statDictionary = {"Player Health" : 30, "Player Damage" : 5, "Guard Health" : 40, "Guard Damage" : 8, "Witch Health" : 35, "Witch Damage" : 10}
powerUps = ["Speed Potion"]

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

def user_power_up_choice(escape):
    iteration = 0
    for i in powerUps:
        print(f"{iteration + 1}. {i}")
        iteration += 1
    power_up_choice = input("Input the name of the power-up you want to use(Write Name Exactly As It Is On The Screen): ")
    if power_up_choice in powerUps:
        if power_up_choice == powerUpOptions[0]:
            statDictionary["Player Health"] += 10
            print(f"Your Health is now {statDictionary['Player Health']}")
        if power_up_choice == powerUpOptions[1]:
            statDictionary["Player Damage"] += 10
            print(f"Your Damage Stat is now {statDictionary['Player Damage']}")
        if power_up_choice == powerUpOptions[2]:
            statDictionary["Player Health"] += 10
            print(f"Your Health is now {statDictionary['Player Health']}")
        if power_up_choice == powerUpOptions[3]:
            statDictionary["Player Damage"] += 10
            print(f"Your Damage Stat is now {statDictionary['Player Damage']}")
        if power_up_choice == powerUpOptions[4]:
            statDictionary["Player Damage"] += 10
            print(f"Your Damage Stat is now {statDictionary['Player Damage']}")
        if power_up_choice == powerUpOptions[5]:
            statDictionary["Player Damage"] += 10
            print(f"Your Damage Stat is now {statDictionary['Player Damage']}")
        if power_up_choice == powerUpOptions[6]:
            statDictionary["Player Damage"] += 10
            print(f"Your Damage Stat is now {statDictionary['Player Damage']}")
        else:
            escape = True
            print("hi")
            powerUps.remove("Speed Potion")
    else:
        print("Invalid Input")
        user_power_up_choice(escape)
        return escape
        

def battle(monster):
    original_monster_health = statDictionary[f"{monster} Health"]
    original_player_health = statDictionary[f"Player Health"]
    print(f"You Are battling the {monster}\nIts stats are:\nHealth = {statDictionary[f"{monster} Health"]}\nDamage = {statDictionary[f"{monster} Damage"]}")
    while statDictionary[f"{monster} Health"] > 0 and statDictionary[f"Player Health"] > 0:
        print("It is your turn!")
        print(f"Your stats are:\nHealth = {statDictionary['Player Health']}\nDamage = {statDictionary['Player Damage']}")
        battle_choice = input("1. Regular\n2. Use Power-up\n3. Wild attack(Double damage but causes 5 damage to you as well)\n4. Attempt to run\nInput the number of the option you wish to choose: ")
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
            else:
                print("You missed!")
            time.sleep(3)
        elif battle_choice == 2:
            if powerUps[0]:
                if powerUps[0] in powerUpOptions:
                    user_power_up_choice(escape)
            else:
                statDictionary["Player Health"] -= 2
                print(f"You have no power ups, but while looking for one you lost 2 Health\nYour new Health is {statDictionary['Player Health']}")
            time.sleep(3)
        elif battle_choice == 3:
            hit = random.randint(1, 2)
            if hit == 1:
                statDictionary["Player Health"] -= 5
                print(f"It was a hit! The {monster} lost {statDictionary['Player Damage'] * 2} health. But in the process you lost 5 Health\nYour new health is {statDictionary['Player Health']}")
                statDictionary[f"{monster} Health"] -= statDictionary["Player Damage"] * 2
            else:
                print("You missed!")
            time.sleep(3)
        elif battle_choice == 4:
            if escape == True:
                print("You escaped!")
                statDictionary[f"{monster} Health"] = original_monster_health
                statDictionary["Player Health"] = original_player_health
            else:
                escape_chance = random.randint(1, 2)
                if escape_chance == 1:
                    escape == True
                else:
                    escape == False
                if escape == True:
                    print("You escaped!")
                    statDictionary[f"{monster} Health"] = original_monster_health
                    statDictionary["Player Health"] = original_player_health
            time.sleep(3)

            

battle("Guard")
