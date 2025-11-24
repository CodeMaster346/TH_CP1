#TH 2nd Squared Numbers Program

numberList = [3, 7, 12, 25, 30, 45, 50, 65, 70, 85, 90, 105, 110, 125, 130, 145, 150, 165, 170, 185, 190, 205, 210, 225, 230, 245, 250, 265, 270, 285]

sqaredNumberList = list(map(lambda x: x**2, numberList))

iteration = 0
for num in numberList:
    print("Original Number: ", numberList[iteration], "Squared Number: ", sqaredNumberList[iteration])
    iteration += 1