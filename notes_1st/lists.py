#TH 2nd list notes
import random
names = ["bob", "jeff", "elon"]

print(names)
print(random.choice(names))
x = names.index("jeff")
print(x)
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

board[1][1] = "X"

print(board[0])
print(board[1])
print(board[2])
#list - changeable, ordered
#tuple - not changeable, ordered
#set - changeable, unordered