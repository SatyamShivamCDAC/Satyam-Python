from dessert import DesertItem

class Candy(DesertItem):
    cost = 50
    def __init__(self,name,quantity):
        super().__init__(name)
        self.quantity = quantity

    def get_cost(self):
        return Candy.cost * (self.quantity/1000)

    def __str__(self):
        return super.__str__() + " Cost : " + str(self.get_cost())

