class Bicycle(object):
    def __init__(self, name, weight, production_cost):
        self.name = name
        self.weight = weight
        self.production_cost = prodution_cost

class Bike_Shops(object):
    def __init__(self, inventory, margin, profit):
        self.margin = margin
        self.profit = profit
        self.inventory = inventory #want this to be a dictionary
        # where each key is a model name, with a value representing stock

class Customers(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.ownsBike = False
