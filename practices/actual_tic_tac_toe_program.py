rowOne = [1, 2, 3]
rowTwo = [4, 5, 6]
rowThree = [7, 8, 9]

win = 0

while win == 0:
    print(f"{rowOne[0]:^5}|{rowOne[1]:^5}|{rowOne[2]:^5}\n ---------------")
    print(f"{rowTwo[0]:^5}|{rowTwo[1]:^5}|{rowTwo[2]:^5}\n ---------------")
    print(f"{rowThree[0]:^5}|{rowThree[1]:^5}|{rowThree[2]:^5}")
    first_player_choice = input("Input the number of the space you want to claim")
    first_player_choice.isdigit()
    if
