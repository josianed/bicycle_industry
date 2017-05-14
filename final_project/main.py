import sys
from bicycles import Bicycle, Customer, Bike_Shop

def main():
    print("Welcome. What would you like to do today?")
    current_choice = main_menu()
    main_menu_options(current_choice)

def main_menu():
    print()
    print(" ----- Main Menu ----- ")
    print("[1] Order bicycles from manufacturer")
    print("[2] Open Bike Shop")
    print("[3] Meet customers")
    print("[4] Go shopping for a new bicycle")
    print("[5] Exit")
    print()
    main_menu_choice = input("Please select an option from the above menu: ")
    return main_menu_choice

def main_menu_options(choice):
    if (choice == "1"):
        current_choice = bicycle_menu()
        bicycle_menu_options(current_choice)
    elif (choice == "2"):
        current_choice = shop_menu()
        shop_menu_options(current_choice)
    elif (choice == "3"):
        current_choice = customer_menu()
        customer_menu_options(current_choice)
    elif (choice == "4"):
        shopping()
    elif (choice == "5"):
        print("Thanks for stopping by. Goodbye!")
        sys.exit()
    else:
        current_choice = main_menu()
        main_menu_options(current_choice)

def bicycle_menu():
    print()
    print(" ----- Bicycle Manufacturer ----- ")
    print("[1] See existing bicycle models")
    print("[2] Order new bicycle model")
    print("[3] Return to main menu")
    print()
    bicycle_menu_choice = input("Please select an option from the above menu: ")
    return bicycle_menu_choice

def bicycle_menu_options(choice):
    if (choice == "1"):
        show_bicycle_list()
        current_choice = bicycle_menu()
        bicycle_menu_options(current_choice)
    elif (choice == "2"):
        create_new_bicycle()
        current_choice = bicycle_menu()
        bicycle_menu_options(current_choice)
    elif (choice == "3"):
        current_choice = main_menu()
        main_menu_options(current_choice)
    else:
        current_choice = bicycle_menu()
        bicycle_menu_options(current_choice)

b1 = Bicycle("A", 20, 50)
b2 = Bicycle("B", 14, 100)
b3 = Bicycle("C", 9, 500)
bicycle_list = [b1, b2, b3] #list of bicycles created by user
def show_bicycle_list():
    if bicycle_list:
        print("Current bicycle models: ")
        print()
        for position, bicycle in enumerate(bicycle_list):
            print("[{}]".format(position + 1))
            bicycle.see_bike()
            print()
    else:
        print("There are currently no bicycles available to view. Please visit manufacturer to place your orders.")

def create_new_bicycle():
    model_name = input("Please enter the new bicycle model's name: ")
    model_weight = None
    while not model_weight:
        try:
            model_weight = int(input("Please enter the new bicycle's weight: "))
            if model_weight < 5 or model_weight > 30:
                print("Please enter a valid weight between 5lbs and 30lbs.")
                model_weight = None
        except ValueError:
            print("Please enter a number.")
    prod_cost = None
    while not prod_cost:
        try:
            prod_cost = int(input("Please enter the new bicycle's production cost: "))
            if prod_cost < 50 or prod_cost > 10000:
                print("Please enter a valid production cost between $50 and $10,000.")
                prod_cost = None
        except ValueError:
            print("Please enter a number.")

    new_bike = Bicycle(model_name, model_weight, prod_cost)
    bicycle_list.append(new_bike)
    print("New bicycle model {} successfully created.".format(model_name))

def shop_menu():
    print()
    print(" ----- Bike Shops ----- ")
    print("[1] See existing bike shops")
    print("[2] Open new bike shop")
    print("[3] Return to main menu")
    print()
    shop_menu_choice = input("Please select an option from the above menu: ")
    return shop_menu_choice

def shop_menu_options(choice):
    if (choice == "1"):
        show_bike_shop_list()
        current_choice = shop_menu()
        shop_menu_options(current_choice)
    elif (choice == "2"):
        create_new_bike_shop()
        current_choice = shop_menu()
        shop_menu_options(current_choice)
    elif (choice == "3"):
        current_choice = main_menu()
        main_menu_options(current_choice)
    else:
        current_choice = shop_menu()
        shop_menu_options(current_choice)

bs1 = Bike_Shop("Bob's Bikes", 20)
bs2 = Bike_Shop("Fixies", 15)
bs3 = Bike_Shop("Speed Supreme", 30)
bs4 = Bike_Shop("Spokes & Wheels", 25)
bike_shop_list = [bs1, bs2, bs3] #list of bicycles created by user
def show_bike_shop_list():
    bs1.add_to_inventory(b1, 5)
    bs1.add_to_inventory(b2, 5)
    bs1.add_to_inventory(b3, 5)
    bs2.add_to_inventory(b1, 15)
    bs3.add_to_inventory(b3, 5)
    bs4.add_to_inventory(b2, 5)
    bs4.add_to_inventory(b3, 5)
    if bike_shop_list:
        print()
        print("Current bike shops in your area: ")
        print()
        for position, shop in enumerate(bike_shop_list):
            print("[{}]".format(position + 1))
            shop.see_shops()
    else:
        print("There are currently no bike shops in your area.")

def create_new_bike_shop():
    shop_name = None
    while not shop_name:
        shop_name = input("Please enter the new bike shop's name: ")
        if len(shop_name) < 3 or len(shop_name) > 70:
            print("Please enter a valid shop name with 3 to 70 characters")
            shop_name = None
    margin = None
    while not margin:
        try:
            margin = int(input("Please enter your shop's margin in %: "))
            if margin < 5 or margin > 70:
                print("Please enter a valid margin between 5% and 70%")
                margin = None
        except ValueError:
            print("Please enter a number.")
    new_shop = Bike_Shop(shop_name, margin)
    bike_shop_list.append(new_shop)
    print("New bike shop {} successfully created.".format(shop_name))
    print()
    print("Now, add some inventory.")
    add_inventory(new_shop)
    add_more = input("Add more inventory? ")
    while add_more == "yes" or add_more == "Yes":
        add_inventory(new_shop)
        add_more = input("Add more inventory? ")
    current_choice = shop_menu()
    shop_menu_options(current_choice)

def add_inventory(new_shop):
    print("Place your order.")
    show_bicycle_list()
    model_number = None
    while not model_number:
        try:
            model_number = int(input("Please select the number of the model you would like to stock: "))
        except ValueError:
            print("Please enter a number.")
            model_number = None
    model_index = model_number - 1
    while model_index < 0 or model_index > len(bicycle_list):
        model_number = int(input("Please select the number of the model you would like to stock: "))
        model_index = model_number - 1
    amount = None
    while not amount:
        try:
            amount = int(input("How many would you like to purchase for your inventory? "))
            if amount < 0 or amount > 200:
                if amount < 0:
                    print("Please enter a number larger or equal to 0.")
                    amount = None
                else:
                    print("Are you sure you want that many?")
                    amount = None
        except ValueError:
            print("Please enter a number.")
            amount = None
    new_shop.add_to_inventory(bicycle_list[model_index], amount)
    print("Successfully purchased {} bicycles of model {} for ${} each".format(amount, bicycle_list[model_index].name, bicycle_list[model_index].production_cost))
    print("Current inventory: ")
    new_shop.check_inventory()
    print("Current profit: ")
    new_shop.check_profit()

def customer_menu():
    print()
    print(" ----- Customers ----- ")
    print("[1] See existing customers")
    print("[2] New customer? Start here!")
    print("[3] Return to main menu")
    print()
    customer_menu_choice = input("Please select an option from the above menu: ")
    return customer_menu_choice

def customer_menu_options(choice):
    if (choice == "1"):
        show_customer_list()
        current_choice = customer_menu()
        customer_menu_options(current_choice)
    elif (choice == "2"):
        greet_customer()
        current_choice = customer_menu()
        customer_menu_options(current_choice)
    elif (choice == "3"):
        current_choice = main_menu()
        main_menu_options(current_choice)
    else:
        current_choice = customer_menu()
        customer_menu_options(current_choice)

c1 = Customer("Kelsey Ryan", 300)
c2 = Customer("Max Frost", 220)
c3 = Customer("Sally May", 3000)
c4 = Customer("Freddie Mac", 1000)
customers_list = {
    "Kelsey Ryan": c1,
    "Max Frost": c2,
    "Sally May": c3,
    "Freddie Mac": c4,
} #List of existing customers
def show_customer_list():
    if customers_list:
        print()
        print("List of existing customers: ")
        print(customers_list.keys())
    else:
        print("No one in this area has shopped for bicycles before.")

def greet_customer():
    new_customer_name = None
    while not new_customer_name:
        new_customer_name = input("Let's add you to the database. What is your full name? ")
        if len(new_customer_name) < 5 or not new_customer_name.isalpha():
            print("Please enter a valid name without symbols or numbers, with at least 5 letters.")
            new_customer_name = None
    budget = None
    while not budget:
        try:
            budget = int(input("What is your budget? "))
            if budget < 50 or budget > 20000:
                if budget < 50:
                    print("You're going to need a bit more money than that for a new bicycle.")
                    budget = None
                else:
                    print("You might want to put a downpayment on a house with that kind of money instead of blowing it on bikes.")
                    budget = None
        except ValueError:
            print("Please enter a number.")
    new_customer = Customer(new_customer_name, budget)
    customers_list[new_customer.name] = new_customer
    print("New customer {} successfully added.".format(new_customer_name))
    return new_customer.name

def shopping():
    shopper = identify_shopper()
    money_left = customers_list[shopper.name].check_fund()
    print("Which shop would you like to visit today?")
    shop = choose_shop(money_left)
    purchase(shopper, shop, money_left)
    current_choice = shopping_menu()
    shopping_menu_options(current_choice)

current_shopper = ["shopper"] #stores the current shopper
def identify_shopper():
    shopper_name = input("Welcome! What is your name? ")
    if shopper_name in customers_list:
        print("Hello {}!".format(shopper_name))
        shopper = customers_list[shopper_name]
        current_shopper[0] = shopper
    else:
        print("Looks like it's your first time visiting us.")
        shopper_name = greet_customer()
        shopper = customers_list[shopper_name]
        current_shopper[0] = shopper
    return shopper

current_shop = ["shop"] #stores the current shop
def choose_shop(money_left):
    show_bike_shop_list()
    print()
    shop_number = None
    while not shop_number:
        try:
            shop_number = int(input("Please select the number of the shop you would like to visit: "))
        except ValueError:
            print("Please enter a number.")
    shop_index = shop_number - 1
    while shop_index < 0 or shop_index > len(bike_shop_list):
        shop_number = int(input("Please select the number of the shop you would like to visit: "))
        shop_index = shop_number - 1
    shop_to_visit = bike_shop_list[shop_index]
    current_shop[0] = shop_to_visit
    print("Welcome to {}.".format(shop_to_visit.name))
    check_affordable_inventory(money_left, shop_to_visit)
    return shop_to_visit

def check_affordable_inventory(fund, shop):
        '''Displays all the bicycles in the store's inventory that a customer can afford given their funds'''
        purchasable_bikes = 0
        for current_bike, number in shop.inventory.items():
            for i in range(len(bicycle_list)):
                bike_to_price = bicycle_list[i]
                if bike_to_price.name == current_bike:
                    if shop.price(bike_to_price) < fund:
                        print("Model {}: {} units".format(current_bike, number))
                        print("Price: ${}".format(shop.price(bike_to_price)))
                        purchasable_bikes += 1
        if purchasable_bikes == 0:
            print("Sorry, the bicycles for sale at this shop exceed your budget.")
            current_choice = shopping_menu()
            shopping_menu_options(current_choice)

def purchase(shopper, shop, money_left):
    try:
        model_to_purchase = input("Please enter the name of the bicycle model you would like to purchase: Model ")
        for bicycle in bicycle_list:
            if model_to_purchase == bicycle.name:
                bike_to_purchase = bicycle
        shop.remove_from_inventory(bike_to_purchase)
        shop.calculate_profit(bike_to_purchase)
        shopper.purchase_bike(bike_to_purchase)
    except:
        print("Whoopsies! I don't recognize that model name. Please try typing it again: ")
        model_to_purchase = input("Please enter the name of the bicycle model you would like to purchase: Model ")
        for bicycle in bicycle_list:
            if model_to_purchase == bicycle.name:
                bike_to_purchase = bicycle
        shop.remove_from_inventory(bike_to_purchase)
        shop.calculate_profit(bike_to_purchase)
        shopper.purchase_bike(bike_to_purchase)
    print("Bike model {} successfully purchased.".format(bike_to_purchase.name))
    shopper.calculate_fund(shop, bike_to_purchase)
    shopper.check_fund()
    print("Remaining inventory: ")
    shop.check_inventory()
    shop.check_profit()

def shopping_menu():
    print()
    print("---- Shopping Menu ----")
    print("[1] Purchase another bicycle")
    print("[2] Done shopping for today - return to main menu")
    print()
    choice = input("Please select an option from the above menu: ")
    return choice

def shopping_menu_options(choice):
    if (choice == "1"):
        shopper = current_shopper[0]
        shopper.see_purchased_bikes()
        money_left = customers_list[shopper.name].check_fund()
        print("Which shop would you like to visit today?")
        shop = choose_shop(money_left)
        purchase(shopper, shop, money_left)
        current_choice = shopping_menu()
        shopping_menu_options(current_choice)
    elif (choice == "2"):
        current_choice = main_menu()
        main_menu_options(current_choice)
    else:
        current_choice = shopping_menu()
        shopping_menu_options(current_choice)

if __name__ == '__main__':
    main()
