import sys

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
        print("4 selected")
    elif (choice == "5"):
        print("Thanks for stopping by. Goodbye!")
        sys.exit()
    else:
        main_menu()

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

bicycle_list = [] #list of bicycles created by user
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
    model_weight = input("Please enter the new bicycle's weight: ")
    prod_cost = int(input("Please enter the new bicycle's production cost: "))
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

bike_shop_list = [] #list of bicycles created by user
def show_bike_shop_list():
    if bike_shop_list:
        print()
        print("Current bike shops in your area: ")
        print()
        for position, shop in enumerate(bike_shop_list):
            print("[{}]".format(position + 1))
            bike_shop.see_shop()
    else:
        print("There are currently no bike shops in your area.")

def create_new_bike_shop():
    shop_name = input("Please enter the new bike shop's name: ")
    margin = input("Please enter your shop's margin in %: ")
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
    model_number = int(input("Please select the number of the model you would like to stock: "))
    model_index = model_number - 1
    while model_index < 0 or model_index > len(bicycle_list):
        model_number = int(input("Please select the number of the model you would like to stock: "))
        model_index = model_number - 1
    amount = int(input("How many would you like to purchase for your inventory? "))
    new_shop.add_to_inventory(bicycle_list[model_index], amount)
    print("Successfully purchased {} bicycles of model {} for ${} each".format(amount, model_index, bicycle_list[model_index].production_cost))
    print("Current inventory: ")
    new_shop.check_inventory()
    print("Current profit: ")
    new_shop.check_profit()

def customer_menu():
    print()
    print(" ----- Customers ----- ")
    print("[1] See existing customers")
    print("[2] Greet new customer")
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

customers_list = [] #List of existing customers
def show_customer_list():
    if customers_list:
        print()
        print("List of existing customers: ")
        print()
        for position, customer in enumerate(customers_list):
            print("[{}]".format(position + 1))
            customer.meet_customers()
    else:
        print("No one in this area has shopped for bicycles before.")

def greet_customer():
    new_customer_name = input("Hello! What is your name? ")
    budget = input("What is your budget? ")
    new_customer = Customer(new_customer_name, budget)
    customers_list.append(new_customer)
    print("New customer {} successfully added.".format(new_customer_name))


class Bicycle(object):
    def __init__(self, name, weight, production_cost):
        self.name = name
        self.weight = weight
        self.production_cost = production_cost

    def see_bike(self):
        ''' Displays a bike's attributes'''
        print("Model {} weighs {} lbs and costs ${} to produce.".format(self.name, self.weight, self.production_cost))

#Tests
# bike1 = Bicycle("Vanquisher", 120, 300)
# print("Model {} weighs {} lbs and cost {} to produce.".format(bike1.name, bike1.weight, bike1.production_cost))

class Bike_Shop(object):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        self.profit = 0
        self.inventory = {}

    shop_list = [] #list of shops created by user
    def save_shop(Bike_Shop):
        '''Saves newly created shop to the shop list'''
        shop_list.append(Bike_Shop)

    def see_shops(self):
        '''Displays all shops that were opened'''
        print("{} has a margin of {}.".format(self.name, self.margin))

    # store_inventory = {} #list of stock available (models + amount)
    def add_to_inventory(self, Bicycle, amount):
        '''Adds a bicycle model and number to stock to the store's inventory, and removes production cost from store profit'''
        self.inventory[Bicycle.name] = amount
        self.profit -= Bicycle.production_cost * amount

    def check_inventory(self):
        '''Displays all the bicycles in the store's inventory with their amount in stock'''
        for bike, number in self.inventory.items():
            print("Model {}: {} units".format(bike, number))

    def price(self, Bicycle):
        '''Calculates bicycle's price based on margin'''
        purchase_cost = Bicycle.production_cost
        sale_price = purchase_cost * (1 + margin)
        return sale_price

    def calculate_profit(self, Bicycle):
        '''Calculates profit from the current sale and adds it to the store's overall profit'''
        current_profit = Bicycle.production_cost * margin
        self.profit += current_profit

    def check_profit(self):
        '''Displays the store's current profit'''
        print("Your store's current profit is ${}.".format(self.profit))

#Tests
# shop1 = Bike_Shop("Larry's Spokes and Wheels", 10)
# print("{} has a margin of {}.".format(shop1.name, shop1.margin))


class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bikes = []

    def meet_customers(self):
        '''Displays a customer's attributes'''
        print("{}".format(self.name))

    def calculate_fund(self, Bike_Shop, Bicycle):
        '''Calculates remaining money in fund after a bicycle is purchased'''
        current_purchase = Bike_Shop.price()
        remaining_fund = self.fund - current_purchase
        return remaining_fund

    def check_fund(self):
        '''Display's the customer's current remaining fund'''
        print("Your remaining fund is {}.".format(self.fund))

#Tests
# customer1 = Customer("Bob", 500)
# print("{} has ${} to spend on a new bike.".format(customer1.name, customer1.fund))
if __name__ == '__main__':
    main()
