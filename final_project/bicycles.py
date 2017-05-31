class Bicycle(object):
    def __init__(self, name, weight, production_cost):
        self.name = name
        self.weight = weight
        self.production_cost = production_cost

class Bike_Shop(object):
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin/100
        self.profit = 0
        self.inventory = {}

    shop_list = [] #list of shops created by user
    def save_shop(Bike_Shop):
        '''Saves newly created shop to the shop list'''
        shop_list.append(Bike_Shop)

    # store_inventory = {} #list of stock available (models + amount)
    def add_to_inventory(self, Bicycle, amount):
        '''Adds a bicycle model and number to stock to the store's inventory, and removes production cost from store profit'''
        self.inventory[Bicycle.name] = amount
        self.profit -= Bicycle.production_cost * amount

    def remove_from_inventory(self, Bicycle):
        '''Removes a bicycle from inventory once it is purchased'''
        stock_remaining = self.inventory[Bicycle.name]
        self.inventory[Bicycle.name] = stock_remaining - 1

    def check_inventory(self):
        '''Displays all the bicycles in the store's inventory with their amount in stock'''
        for bike, number in self.inventory.items():
            print("Model {}: {} units".format(bike, number))

    def price(self, Bicycle):
        '''Calculates bicycle's price based on margin'''
        purchase_cost = Bicycle.production_cost
        sale_price = purchase_cost * (1 + self.margin)
        return sale_price

    def calculate_profit(self, Bicycle):
        '''Calculates profit from the current sale and adds it to the store's overall profit'''
        current_profit = Bicycle.production_cost * self.margin
        self.profit += current_profit

    def check_profit(self):
        '''Displays the store's current profit'''
        print("{} has a current profit of ${}.".format(self.name, self.profit))

class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.bikes = []

    def see_purchased_bikes(self):
        '''Displays a list of bikes that the customer owns'''
        for bike in self.bikes:
            print("You currently own the following bicycles: ")
            print("Model {}".format(bike.name))

    def calculate_fund(self, Bike_Shop, Bicycle):
        '''Calculates remaining money in fund after a bicycle is purchased'''
        current_purchase = Bike_Shop.price(Bicycle)
        print("Bike to purchase costs ${}".format(current_purchase))
        self.fund -= current_purchase

    def check_fund(self):
        '''Displays the customer's current remaining fund'''
        print("Your remaining fund is ${}".format(self.fund))
        return self.fund

    def purchase_bike(self, Bicycle):
        '''Adds purchased bike to customer's personal bike list'''
        self.bikes.append(Bicycle)
