#TH 2nd Flexible Calculator Program
import math

operations = ["sum", "average", "max", "min", "product"]
numbers = []

def product_calculation(end_index):
    math.prod(numbers[0, end_index])



def main():
    print("Welcome to the Flexible Calculator")
    print("====================================================================================")
    print("sum\naverage\nmax\nmin\nproduct")
    operation = input("Type the operation you wish to use: ")
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
        end_index = len(numbers) - 1
        product_calculation(end_index)
        
        



main()