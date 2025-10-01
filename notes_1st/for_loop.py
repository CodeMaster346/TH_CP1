# TH 2nd for loops notes
import time

nums = [1,1234, 345, 6, 4, 7, 56, 76, 4, 4265, 65, 2354, 456, 376, 348, 1340985643]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is hald of {num}. And it is still a large number!")
    else:
        print(num)

print("we completed all the numbers!")
time.sleep(3)
for x in range(1, 10):
    print(x)
time.sleep(3)
for x in range(2, 11, 2):
    print(x)
time.sleep(3)
for x in range(10, 0, -1):
    print(x)
    time.sleep(1)