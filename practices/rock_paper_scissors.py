#TH 2nd Rock Paper Scissors
import random
bot_desision = random.randint(1,3)




user_decision = int(input("1. rock\n2. Paper\n3. Scissors\nInput the number of the option you want to choose: "))

if user_decision == 1 and bot_desision == 2:
    print("placeholder for player lose")
elif user_decision == 1 and bot_desision == 1:
    print("placeholder for a draw")
elif user_decision == 1 and bot_desision == 3:
    print("placeholder for a player win")
elif user_decision == 2 and bot_desision == 2:
    print("placeholder for a draw")
elif user_decision == 2 and bot_desision == 1:
    print("placeholder for a player win")
elif user_decision == 2 and bot_desision == 3:
    print("placeholder for a player lose")
elif user_decision == 3 and bot_desision == 2:
    print("placeholder for a player win")
elif user_decision == 3 and bot_desision == 1:
    print("placeholder for a player lose")
elif user_decision == 3 and bot_desision == 3:
    print("placeholder for a draw")
