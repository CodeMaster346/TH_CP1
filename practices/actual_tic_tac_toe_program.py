board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
    print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
    print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
    first_player_choice = int(input("\nX player, input the number of the space you want to claim: "))
    
    if first_player_choice not in board:
        while first_player_choice not in board:
            print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
            print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
            print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
            first_player_choice = int(input("\nX player, input the number of the space you want to claim: "))
    
    board[first_player_choice - 1] = "X"

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit


    print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
    print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
    print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
    second_player_choice = int(input("\nO player, Input the number of the space you want to claim: "))
    
    if second_player_choice not in board:
        while first_player_choice not in board:
            print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
            print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
            print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
            first_player_choice = int(input("\nO player, input the number of the space you want to claim: "))
    
    board[first_player_choice - 1] = "X"

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print(f"{board[0]:^5}|{board[1]:^5}|{board[2]:^5}\n ---------------")
        print(f"{board[3]:^5}|{board[4]:^5}|{board[5]:^5}\n ---------------")
        print(f"{board[6]:^5}|{board[7]:^5}|{board[8]:^5}")
        print("X Player Wins!")
        raise SystemExit