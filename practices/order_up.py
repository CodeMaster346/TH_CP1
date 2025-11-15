#TH 2nd Order Up

def receipt(new_price):
    print(f"Drink: {drink}\nMain Course: {main_course}\nSides: {side1}, {side2}\nTotal Price (with tax): ${new_price}")

def tax_calc(price):

    price = ((1/100) * price) + price
    new_price = f"{price:.2f}"
    receipt(new_price)
    
    
drinkChoices = {'Coke' : 1.00, 'Root Beer' : 0.50, 'Water' : 0, 'Lemonade' : 3.00}
mainCourses = {'Burger' : 10.00, 'Nachos' : 8.00, 'Shredded Pork' : 15.00, 'Chicken Sandwich' : 10.00, 'Full Pizza' : 20.00}
sideDishes = {'Salad' : 5.00, 'Fries' : 6.00, 'Cheese Fries' : 10.00}

print("Coke\nRoot Beer\nWater\nLemonade")
drink = input("What drink would you like? ")

print("Burger\nNachos\nShredded Pork\nChicken Sandwich\nFull Pizza")
main_course = input("What main course would you like? ")

print("Salad\nFries\nCheese Fries")
side1 = input("What side would you like for your first side? ")

print("Salad\nFries\nCheese Fries")
side2 = input("What side would you like for your second side? ")

price = drinkChoices[f'{drink}'] + mainCourses[f'{main_course}'] + sideDishes[f'{side1}'] + sideDishes[f'{side2}']
tax_calc(price)