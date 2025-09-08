while True:
    user_choice = int(input("1. New equation\n2. Exit\nInput the number for the option you want to choose: "))
    if user_choice == 1:
        input_1 = float(input("Input a number: "))
        input_2 = float(input("Input another number: "))
        equation_sign = input("What type of equation do you want (including modulo and exponent)? ").strip().lower()
        if equation_sign == "multiplication":
            print(f"{input_1} x {input_2} = {round(input_1 * input_2):.2f}")
        elif equation_sign == "division":
            print(f"{input_1} x {input_2} = {round(input_1 / input_2):.2f}")
