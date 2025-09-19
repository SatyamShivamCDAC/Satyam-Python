from dessert import DesertItem

class Cookie(DesertItem):
    cost = 10
    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def get_cost(self):
        return self.quantity/12 * Cookie.cost

    def __str__(self):
        return super.__str__() + " Cost : " + str(self.get_cost())

