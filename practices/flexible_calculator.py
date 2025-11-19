#TH 2nd Flexible Calculator Program
import math

operations = ["sum", "average", "max", "min", "product"]
numbers = []

def product_calculation(*args):
    end_index = len(numbers)
    all_numbers = numbers[0:end_index]
    answer = math.prod(all_numbers)
    print(f"The product of these numbers is {answer}")
    del numbers[0:end_index]

def min_calculation(*args):
    end_index = len(numbers)
    all_numbers = numbers[0:end_index]
    answer = min(all_numbers)
    print(f"The minimum of these numbers is {answer}")
    del numbers[0:end_index]

def max_calculation(*args):
    end_index = len(numbers)
    all_numbers = numbers[0:end_index]
    answer = max(all_numbers)
    print(f"The maximum of these numbers is {answer}")
    del numbers[0:end_index]

def average_calculation(*args):
    end_index = len(numbers)
    all_numbers = numbers[0:end_index]
    first_answer = sum(all_numbers)
    final_answer = first_answer/end_index
    print(f"The average of these numbers is {final_answer}")
    del numbers[0:end_index]

def sum_calculation(*args):
    end_index = len(numbers)
    all_numbers = numbers[0:end_index]
    answer = sum(all_numbers)
    print(f"The sum of these numbers is {answer}")
    del numbers[0:end_index]

def main():
    while True:
        print("Welcome to the Flexible Calculator")
        print("====================================================================================")
        print("sum\naverage\nmax\nmin\nproduct")
        operation = input("Type the operation you wish to use(You might have to re-run the code occasionally to get the right answer): ")
        if operation not in operations:
            while operation not in operations:
                print("Invalid Input")
                print("====================================================================================")
                print("sum\naverage\nmax\nmin\nproduct")
                operation = input("Type the operation you wish to use: ")
        print("====================================================================================")
        print("You can now enter the numbers you wish to use. Type done when you are finished.")
        while True:
            user_input = input("Input a number, or type done: ")
            if user_input == "done":
                break
            elif not user_input.isdigit():
                while not user_input.isdigit():
                    print("Invalid Input")
                    user_input = input("Input a number, or type done: ")
            if user_input.isdigit():
                user_input = int(user_input)
                numbers.append(user_input)
        if operation == "product":
            product_calculation()
        elif operation == "min":
            min_calculation()
        elif operation == "max":
            max_calculation()
        elif operation == "average":
            average_calculation()
        else:
            sum_calculation()
        continuing = input("Would you like to continue (Y/N)? ")
        if continuing != "Y" and continuing != "N":
            while True:
                print("Invalid Input")
                continuing = input("Would you like to continue (Y/N)? ")
                if continuing == "Y" or continuing == "N":
                    break
        elif continuing == "N":
            raise SystemExit
        else:
            continue        


main()