#TH 2nd factorial program
#DOWNLOAD math capabilities to the program
#
#CONTAINER for functionality with the numbers
#LOOP to keep code running till user types 'end'
#   PROMPT user to input the number they want to use, or type end
#   SET number AS the input the user gives
#   IF number IS SET AS end THEN
#       EXIT code
#   ELSE, IF number IS NOT SET AS a digit THEN
#       LOOP that keeps running till user inputs a number or 'end'
#           DISPLAY Invalid Input
#           PROMPT user again to input a number or 'end'
#           SET number AS the given input
#           IF number IS SET AS 'end' THEN
#               EXIT code
#   make number a NUMBER
#
#    IF number IS SET AS 0 THEN
#        DISPLAY 0 = 1
#    ELSE, if this condition is not met, THEN
#        SET original_number AS number
#        SET iteration AS 1
#        LOOP until iteration IS EQUAL TO original_number
#            IF iteration IS SET AS 1 AND origional_number IS SET AS 1 THEN
#                ADD number to CONTAINER
#                SET iteration AS iteration + 1
#            ELSE, IF iteration IS SET AS 1 THEN
#                ADD number to CONTAINER
#                ADD 'x' to CONTAINER
#                SET iteration AS iteration + 1
#            ELSE, IF iteration IS EQUAL TO origional_number THEN
#                SET number AS number - 1
#                ADD number to CONTAINER
#                SET iteration AS iteration + 1
#            ELSE, if none of these conditions are met, THEN
#                SET number AS number - 1
#                ADD number to CONTAINER
#                ADD 'x' to CONTAINER
#                SET iteration AS iteration + 1
#
#        DISPLAY the CONTAINER in a readable way, THEN DISPLAY the answer with an equal sign before it
#    CLEAR the container
#    CONTINUE the loop till the user types 'end'



import math

functionalityList = []
while True:
    number = input("Input the number you wish to factor, or type end to exit: ")
    if number == "end":
        raise SystemExit
    elif not number.isdigit():
        while not number.isdigit:
            print("Invalid Input")
            number = input("Input the number you wish to factor, or type end to exit: ")
            if number == "end":
                raise SystemExit
    number = int(number)

    if number == 0:
        print("0 = 1")
    else:
        original_number = number
        iteration = 1
        while iteration <= original_number:
            if iteration == 1 and original_number == 1:
                functionalityList.append(number)
                iteration += 1
            elif iteration == 1:
                functionalityList.append(number)
                functionalityList.append("x")
                iteration += 1
            elif iteration == original_number:
                number = number - 1
                functionalityList.append(number)
                iteration += 1
            else:
                number = number - 1
                functionalityList.append(number)
                functionalityList.append("x")
                iteration += 1

        print(' '.join(map(str, functionalityList)), "=", math.factorial(original_number))
    functionalityList.clear()
