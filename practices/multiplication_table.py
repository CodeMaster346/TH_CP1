mult_nums = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

iteration = 1

print("  X  |   1   |   2   |   3     4     5     6     7     8     9    10    11    12\n")
for mult_num in mult_nums:
    print(f"{mult_nums[0] * iteration:^5}|{mult_nums[1] * iteration:^5}|{mult_nums[2] * iteration:^5}|{mult_nums[3] * iteration:^5}|{mult_nums[4] * iteration:^5}|{mult_nums[5] * iteration:^5}|{mult_nums[6] * iteration:^5}|{mult_nums[7] * iteration:^5}|{mult_nums[8] * iteration:^5}|{mult_nums[9] * iteration:^5}|{mult_nums[10] * iteration:^5}|{mult_nums[11] * iteration:^5}|{mult_nums[12] * iteration:^5}\n")
    iteration = iteration + 1
