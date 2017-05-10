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
        print("2 selected")
    elif (choice == "3"):
        print("3 selected")
    elif (choice == "4"):
        print("4 selected")
    elif (choice == "5"):
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
        for bicycle in bicycle_list:
            bicycle.see_bike()
    else:
        print("There are currently no bicycles available to view.")

def create_new_bicycle():
    model_name = input("Please enter the new bicycle model's name: ")
    model_weight = input("Please enter the new bicycle's weight: ")
    prod_cost = input("Please enter the new bicycle's production cost: ")
    new_bike = Bicycle(model_name, model_weight, prod_cost)
    bicycle_list.append(new_bike)
    print("New bicycle model {} successfully created.".format(model_name))


class Bicycle(object):
    def __init__(self, name, weight, production_cost):
        self.name = name
        self.weight = weight
        self.production_cost = production_cost


    # bicycle_list = [] #list of bicycles created by user
    # def save_bike(Bicycle):
    #     '''Saves a newly created bicycle to the bicycle list'''
    #     bicycle_list.append(Bicycle)

    def see_bike(self):
        ''' Displays a bike's attributes'''
        print("{} weighs {} lbs and costs {} to produce.".format(self.name, self.weight, self.production_cost))

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

        def see_shops():
            '''Displays all shops that were opened'''
            for shop in shop_list.items():
                print(shop, sep=", ")

        store_inventory = {} #list of stock available (models + amount)
        def add_inventory(self, Bicycle, amount):
            '''Adds a bicycle model and its amount to the store's inventory, and removes production cost from store profit'''
            store_inventory[Bicycle.name] = amount
            self.profit -= Bicycle.production_cost

        def check_inventory():
            '''Displays all the bicycles in the store's inventory with their amount in stock'''
            for bike, number in store_inventory.items():
                print(bike, number, sep=": ")

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
            print("Your store's current profit is {}.".format(self.profit))

#Tests
# shop1 = Bike_Shop("Larry's Spokes and Wheels", 10)
# print("{} has a margin of {}.".format(shop1.name, shop1.margin))


class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bikes = []

    customers = [] #List of customers
    def save_customer(Customer):
        '''Saves a new customer to the customer list'''
        customer.append(Customer)

    def meet_customers():
        '''Displays all the customers'''
        for customer in customers.items():
            print(customer, sep=", ")

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
