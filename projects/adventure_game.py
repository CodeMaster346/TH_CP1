#TH 2nd Final Project
import time
import random

escape = False
wins = 1
check_win = 2

powerUpOptions = ["Health Potions", "Strength Potions", "Extra Armor", "Sword", "Bow and Arrow", "Wizard staff", "Firebending Potion", "Speed Potion"]
statDictionary = {"Player Health" : 30, "Player Damage" : 10, "Guard Health" : 40, "Guard Damage" : 8, "Witch Health" : 35, "Witch Damage" : 10}
powerUps = []
endings = ["_____________", "_____________", "_____________", "_____________"]

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

def win_or_lose(check_win, wins):
    if check_win == 1:
        if wins == 1:
            powerUps.append("Key")
            print("You got the key.")
        time.sleep(2)
        print("You won and got 3 power-ups!")
        power_up_1 = powerUpOptions[random.randint(1, 8) - 1]
        power_up_2 = powerUpOptions[random.randint(1, 8) - 1]
        power_up_3 = powerUpOptions[random.randint(1, 8) - 1]
        powerUps.append(power_up_1)
        powerUps.append(power_up_2)
        powerUps.append(power_up_3)
    else:
        print("You Lost")
        restart()
        return


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
        

def battle(monster, check_win, wins):
    original_monster_health = statDictionary[f"{monster} Health"]
    original_player_health = statDictionary[f"Player Health"]
    print(f"You Are battling the {monster}\nIts stats are:\nHealth = {statDictionary[f"{monster} Health"]}\nDamage = {statDictionary[f"{monster} Damage"]}")
    time.sleep(2)
    while statDictionary[f"{monster} Health"] > 0 and statDictionary[f"Player Health"] > 0:
        print("It is your turn!")
        time.sleep(2)
        print(f"Your stats are:\nHealth = {statDictionary['Player Health']}\nDamage = {statDictionary['Player Damage']}")
        time.sleep(2)
        battle_choice = input("1. Regular\n2. Use Power-up\n3. Wild attack(Double damage but causes 5 damage to you as well)\n4. Attempt to run\nInput the number of the option you wish to choose: ")
        num = battle_choice.isdigit()
        if num == True:
            battle_choice = int(battle_choice)
        else:
            while num == False:
                print("Invalid Input")
                time.sleep(2)
                battle_choice = input("1. Regular\n2. Use Power-up\n3. Wild attack(Double damage but causes damage to you as well)\n4. Attempt to run\nInput the number of the option you wish to choose: ")
                num = battle_choice.isdigit()
                if num == True:
                    battle_choice = int(battle_choice)

        if battle_choice == 1:
            hit = random.randint(1, 2)
            if hit == 1:
                time.sleep(2)
                print(f"It was a hit! The {monster} lost {statDictionary['Player Damage']} health.")
                statDictionary[f"{monster} Health"] -= statDictionary["Player Damage"]
            else:
                time.sleep(2)
                print("You missed!")
            time.sleep(3)
        elif battle_choice == 2:
            if 0 < len(powerUps):
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
                time.sleep(2)
                print(f"It was a hit! The {monster} lost {statDictionary['Player Damage'] * 2} health. But in the process you lost 5 Health\nYour new health is {statDictionary['Player Health']}")
                statDictionary[f"{monster} Health"] -= statDictionary["Player Damage"] * 2
            else:
                time.sleep(2)
                print("You missed!")
            time.sleep(3)
        elif battle_choice == 4:
            if escape == True:
                time.sleep(2)
                print("You escaped!")
                statDictionary[f"{monster} Health"] = original_monster_health
                statDictionary["Player Health"] = original_player_health
                return
            else:
                escape_chance = random.randint(1, 2)
                if escape_chance == 1:
                    escape == True
                else:
                    escape == False
                if escape == True:
                    time.sleep(2)
                    print("You escaped!")
                    statDictionary[f"{monster} Health"] = original_monster_health
                    statDictionary["Player Health"] = original_player_health
                    return
                else:
                    time.sleep(2)
                    print("You didnt escape and took a fatal blow.")
                    restart()
                    return
            time.sleep(3)
        print(f"It is the {monster}'s turn!")
        hit = random.randint(1, 2)
        if hit == 1:
            print(f"The monster hit you and you lost {statDictionary[f"{monster} Damage"]}")
            statDictionary["Player Health"] -= statDictionary[f"{monster} Damage"]
        else:
            print(f"The {monster} missed")
    if statDictionary[f"{monster} Health"] <= 0:
        check_win = 1
    else:
        check_win == 2
    statDictionary["Player Health"] = original_player_health
    statDictionary[f"{monster} Health"] = original_monster_health
    win_or_lose(check_win, wins)

def main(check_win):
    while True:
        print("You are the crown prince of the kingdom of Xenon and have always wanted to go and see the world, but your parents say that your duties are more important. So you decided you will attempt to escape the kingdom once everyone goes to sleep.")
        time.sleep(2)
        play_or_exit = int(input("1. Start Game\n2. Exit\n3. Show the endings you have collected\nInput the number for the option you wish to choose: "))

        if play_or_exit == 1:
            time.sleep(2)
            escape_choice = int(input("Everyone is now asleep\n1. Use the tattered bedsheets to climb down the castle walls\n2. Sneak through the castle halls\n3. Wake up your siblings and get them to help you\nInput the number for the escape option you wish to choose: "))

            if escape_choice == 1:
                print("You started climbing down the walls but the bedsheets ripped and you fell to your death.")
                time.sleep(2)
                restart()
            elif escape_choice == 2:
                steal_keys = input("Do you want to attempt stealing the guards keys(Y/N)? ")
                steal_keys = steal_keys.upper()
                if steal_keys == "Y":
                    for i in range(1):
                        wins = 1
                        battle("Guard", check_win, wins)
                    statDictionary["Player Health"] += 10
                else:
                    wins = 2
                    time.sleep(2)
                    bright_or_dark = int(input("1. Go through the brightly lit, guarded area thst goes straight to the gates\n2. Go through the dark alley that smells funny\nInput the number for the path you wish to choose: "))

                    if bright_or_dark == 1:
                        print("You got caught by 5 members of the Royal Army")
                        for i in range(5):
                            battle("Guard", check_win, wins = 2)
                        print("You escaped using the risky ending! Congrats!")
                        if endings[0] == "_____________":
                            endings[0] = "Risky"
                        elif endings[1] == "_____________":
                            endings[1] = "Risky"
                        elif endings[2] == "_____________":
                            endings[2] = "Risky"
                        else:
                            endings[3] = "Risky"
                    elif bright_or_dark == 2:
                        time.sleep(2)
                        light_match = input("Do you want to light a match to see better(Y/N)? ")
                        light_match = light_match.upper()
                        if light_match == "Y":
                            time.sleep(2)
                            print("That funny smell was gas, so when you lit the match you exploded.")
                            restart()
                        else:
                            time.sleep(2)
                            go_into_the_tavern = input("You came across a tavern in the alley, do you want to go in(Y/N)? ")
                            go_into_the_tavern = go_into_the_tavern.upper()
                            if go_into_the_tavern == "Y":
                                time.sleep(2)
                                print("You went in to the tavern and found a power-up in the trash.")
                                power_up = powerUpOptions[random.randint(1, 8) - 1]
                                powerUps.append(power_up)
                            time.sleep(2)
                            print("You came across a house and went in.")
                            time.sleep(1)
                            stay = input("Do you want to stay and see what the amazing smell is(Y/N)?")
                            stay = stay.upper()
                            if stay == "Y":
                                time.sleep(2)
                                print("You stayed and ran into a witch that tries to cook you.")
                                time.sleep(1)
                                stab = int(input("1. Pour boiling water on the witch\n2. Stab the witch with a knife\nInput the number for the option you wish to choose"))

                                if stab == 1:
                                    time.sleep(2)
                                    print("The witch melted and you ran out the back door.")
                                else:
                                    time.sleep(2)
                                    print("Stabing the witch just made the witch mad at you.")
                                    battle("Witch", check_win, wins = 2)
                            time.sleep(2)
                            print("You escaped and got to the gate, but you ran into a guard")
                            time.sleep(2)
                            battle("Guard", check_win, wins = 2)
                            if "Key" in powerUps:
                                time.sleep(2)
                                print("You had the key and escaped through the gate using the battle ready ending! Congrats!")
                                if endings[0] == "_____________":
                                    endings[0] = "Battle Ready"
                                elif endings[1] == "_____________":
                                    endings[1] = "Battle Ready"
                                elif endings[2] == "_____________":
                                    endings[2] = "Battle Ready"
                                else:
                                    endings[3] = "Battle Ready"
                            else:
                                time.sleep(2)
                                print("You climbed the wall and ran into your parents who ordered 2 guards to capture you.")
                                for i in range(2):
                                    battle("Guard", check_win, wins = 2)
                                time.sleep(2)
                                print("You escaped using the unprepared ending. Congrats I guess.")
                                if endings[0] == "_____________":
                                    endings[0] = "Unprepared"
                                elif endings[1] == "_____________":
                                    endings[1] = "Unprepared"
                                elif endings[2] == "_____________":
                                    endings[2] = "Unprepared"
                                else:
                                    endings[3] = "Unprepared"
            if escape_choice == 3:
                time.sleep(2)
                print("You woke up you siblings and you decided to take the family plane to get out")
                statDictionary["Player Health"] = statDictionary["Player Health"] * 3
                original_player_health = statDictionary["Player Health"]
                time.sleep(2)
                print("You ran into 10 air force pilot guards.")
                wins = 2
                for i in range(10):
                    battle("Guard", check_win, wins = 2)
                    statDictionary["Player Health"] = original_player_health
                time.sleep(2)
                print("You escaped using the plane ending! Congrats!")
                if endings[0] == "_____________":
                    endings[0] = "Plane"
                elif endings[1] == "_____________":
                    endings[1] = "Plane"
                elif endings[2] == "_____________":
                    endings[2] = "Plane"
                else:
                    endings[3] = "Plane"
            else:
                print("You stupid, You entered an invalid number")
        elif play_or_exit == 2:
            raise SystemExit
        elif play_or_exit == 3:
            print(endings)
        else:
            print("You stupid")

main(check_win)