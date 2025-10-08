#TH 2nd Rock Paper Scissors
import random
import time

while True:
    bot_desision = random.randint(1,3)
    print("  \n _.-.-.-.\n:_|_|_|_|_\n|_|_|\__  \ \n|    . '  |\n|   (    /\n \______/")
    print("1. Rock")
    print("   _.-._\n _| | | |\n| | | | |\n| | | | |\n| : ' : | .-.\n|       |/ /\n|     ,-' /\n|    /    |\n|         /\n \_______/")
    print("2. Paper")
    print("    .-.\n    | |    / ) \n    | |   / /\n    | |  / /\n _.-| |_/ /\n: \( \   /\n|\_)\ \  |\n|    ] \ |\n|   (    /\n \______/")
    print("3. Scissors")
    user_decision = int(input("Input the number of the option you want to choose or type 4 if you wish to exit: "))

    if user_decision == 1 and bot_desision == 2:
        print("=======================================")
        print("\033[31mYou chose:\n\n\n _.-.-.-.\n:_|_|_|_|_\n|_|_|\__  \ \n|    . '  |\n|   (    /\n \______/\033[0m\n")
        print("=======================================")
        print("\033[32mThe Bot chose:\n\n\n   _.-._\n _| | | |\n| | | | |\n| | | | |\n| : ' : | .-.\n|       |/ /\n|     ,-' /\n|    /    |\n|         /\n \_______/\033[0m")
        print("=======================================")
        print("\nYou lost!")
        time.sleep(5)
    elif user_decision == 1 and bot_desision == 1:
        print("=======================================")
        print("\033[31mYou chose:\n\n\n _.-.-.-.\n:_|_|_|_|_\n|_|_|\__  \ \n|    . '  |\n|   (    /\n \______/\n\033[0m")
        print("=======================================")
        print("\033[32mThe Bot chose:\n\n\n _.-.-.-.\n:_|_|_|_|_\n|_|_|\__  \ \n|    . '  |\n|   (    /\n \______/\033[0m")
        print("=======================================")
        print("\nIt was a draw!")
        time.sleep(5)
    elif user_decision == 1 and bot_desision == 3:
        print("=======================================")
        print("\033[31mYou chose:\n\n\n _.-.-.-.\n:_|_|_|_|_\n|_|_|\__  \ \n|    . '  |\n|   (    /\n \______/\n\033[0m")
        print("=======================================")
        print("\033[32mThe Bot chose:\n\n\n    .-.\n    | |    / ) \n    | |   / /\n    | |  / /\n _.-| |_/ /\n: \( \   /\n|\_)\ \  |\n|    ] \ |\n|   (    /\n \______/\033[0m")
        print("=======================================")
        print("\nYou won! Congrats!")
        time.sleep(5)
    elif user_decision == 2 and bot_desision == 2:
        print("=======================================")
        print("\033[31mYou chose:\n\n\n   _.-._\n _| | | |\n| | | | |\n| | | | |\n| : ' : | .-.\n|       |/ /\n|     ,-' /\n|    /    |\n|         /\n \_______/\033[0m")
        print("=======================================")
        print("\033[32mThe Bot chose:\n\n\n   _.-._\n _| | | |\n| | | | |\n| | | | |\n| : ' : | .-.\n|       |/ /\n|     ,-' /\n|    /    |\n|         /\n \_______/\033[0m")
        print("=======================================")
        print("\nIt was a draw!")
        time.sleep(5)
    elif user_decision == 2 and bot_desision == 1:
        print("=======================================")
        print("\033[31mYou chose:\n\n\n   _.-._\n _| | | |\n| | | | |\n| | | | |\n| : ' : | .-.\n|       |/ /\n|     ,-' /\n|    /    |\n|         /\n \_______/\033[0m")
        print("=======================================")
        print("\033[32mThe Bot chose:\n\n\n _.-.-.-.\n:_|_|_|_|_\n|_|_|\__  \ \n|    . '  |\n|   (    /\n \______/\033[0m")
        print("=======================================")
        print("You Won! Congrats!")
        time.sleep(5)
    elif user_decision == 2 and bot_desision == 3:
        print("=======================================")
        print("\033[31mYou chose:\n\n\n   _.-._\n _| | | |\n| | | | |\n| | | | |\n| : ' : | .-.\n|       |/ /\n|     ,-' /\n|    /    |\n|         /\n \_______/\033[0m")
        print("=======================================")
        print("\033[32mThe Bot chose:\n\n\n    .-.\n    | |    / ) \n    | |   / /\n    | |  / /\n _.-| |_/ /\n: \( \   /\n|\_)\ \  |\n|    ] \ |\n|   (    /\n \______/\033[0m")
        print("=======================================")
        print("You lost!")
        time.sleep(5)
    elif user_decision == 3 and bot_desision == 2:
        print("placeholder for a player win")
        time.sleep(5)
    elif user_decision == 3 and bot_desision == 1:
        print("placeholder for a player lose")
        time.sleep(5)
    elif user_decision == 3 and bot_desision == 3:
        print("placeholder for a draw")
        time.sleep(5)
    elif user_decision == 4:
        raise SystemExit
    else:
        print("Invalid Input")
        time.sleep(5)