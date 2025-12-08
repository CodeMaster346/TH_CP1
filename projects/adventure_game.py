#TH 2nd Final Project
import time
import random

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
    print()


powerUpOptions = ["Health Potions", "Strength Potions", "Extra Armor", "Sword", "Bow and Arrow", "Wizard staff", "Firebending Potion", "Speed Potion"]
statDictionary = {"Player Health", 30, "Player Damage", 5, "Guard Health", 40, "Guard Damage", 8, "Witch Health", 35, "Witch Damage", 10}
powerUps = []

while True:
    
