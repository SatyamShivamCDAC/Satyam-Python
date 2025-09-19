from icecream import Icecream

class Sundae(Icecream):
    def __init__(self,name,quantity):
        self.name = name
        self.quantity =quantity

    def get_cost(self):
        return super().get_cost() + 20

    def __str__(self):
        super.__str__()