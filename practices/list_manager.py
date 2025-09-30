# TH 2nd Shopping list Manager

shopping_items = []

while True:
    action = input("1. Add item to shopping list\n2. Mark item as done\n3. Remove item from shopping list\n4. Show shopping list\n5. Exit\nInput the number for the option you want to choose: ")
    if action == "1": 
        print("---------------------------------------------")
        item = input("What item would you like to add to your shopping list? ")
        print("---------------------------------------------")
        print("---------------------------------------------")
        print("Item added!")
        print("---------------------------------------------")
        shopping_items.append(item)
    elif action == "2":
        print("---------------------------------------------")
        item_choice = input("What is the item you would like to mark as finished? ")
        print("---------------------------------------------")
        if item_choice in shopping_items:
            print("---------------------------------------------")
            print("Item marked!")
            print("---------------------------------------------")
            shopping_items[item_choice] = f"*{item_choice}"
        else:
            print("---------------------------------------------")
            print("Item not recognised.")
            print("---------------------------------------------")
    elif action == "3":
        item_choice = input("What item would you like to remove? ")
        if item_choice in shopping_items:
            print("---------------------------------------------")
            print("Item removed!")
            print("---------------------------------------------")
            shopping_items.remove(item_choice)
        else:
            print("---------------------------------------------")
            print("Item not recognised.")
            print("---------------------------------------------")                        
    elif action == "4":
        if len(shopping_items) > 0:
            print("---------------------------------------------")
            print("All items with a * next to it have been marked as finished")
            print("---------------------------------------------")
            print("---------------------------------------------")
            for i, item in enumerate(shopping_items, 1):
                print(f"{i}. {item}")
            print("---------------------------------------------")
        else:
            print("---------------------------------------------")
            print("List empty")            
            print("---------------------------------------------")
    elif action == "5":
        print("---------------------------------------------")
        print("Bye!")
        print("---------------------------------------------")
        raise SystemExit
    else:
        print("---------------------------------------------")
        print("Invalid input")
        print("---------------------------------------------")