#TH 2nd Final Project
import time
import random

powerUpOptions = ["Health Potions", "Strength Potions", "Extra Armor", "Sword", "Bow and Arrow", "Wizard staff", "Firebending Potion", "Speed Potion"]
statDictionary = {"Player Health" : 30, "Player Damage" : 5, "Guard Health" : 40, "Guard Damage" : 8, "Witch Health" : 35, "Witch Damage" : 10}
powerUps = []

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
        hit = random.randint(1, 2)
        if battle_choice == 1:
            hit = random.randint(1, 2)
            if hit == 1:
                print(f"It was a hit! The {monster} lost {statDictionary['Player Damage']} health.")
                statDictionary[f"{monster} Health"] -= statDictionary["Player Damage"]
                print(statDictionary[f"{monster} Health"])
            else:
                print("hi")

battle("Guard")
    
