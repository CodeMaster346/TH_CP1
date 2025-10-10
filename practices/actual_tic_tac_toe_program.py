board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

win = 0

while win == 0:
    print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
    print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
    print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
    first_player_choice = int(input("\nInput the number of the space you want to claim: "))
    
    if first_player_choice not in board:
        while first_player_choice not in board:
            print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
            print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
            print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
            first_player_choice = int(input("\nInput the number of the space you want to claim: "))
    else:
        print("hello")
