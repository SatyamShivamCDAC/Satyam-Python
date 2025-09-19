from Assignments.class_asignments.day8.shoppingKart.icecream import Icecream
from Assignments.class_asignments.day8.shoppingKart.sundae import Sundae
from dessert import DesertItem
from candy import Candy
from cookie import Cookie
class Checkout():

    def __init__(self):
        cookie1 = Cookie('Choco Cookies',18)
        cookie2 = Cookie('Orange Cookies',18)
        candy1 = Candy('Mango Candies',200)
        candy2 = Candy('Chocolate Candies',500)
        icecream1 = Icecream('American nuts',2)
        icecream2 = Icecream('Chocochips Icecream', 1)
        sundae1 = Sundae('Vallina Sundae',1)
        sundae2 = Sundae('Chocolate Sundae',1 )
        self.deserts = [cookie1,cookie2,candy1,candy2,icecream1,icecream2,sundae1,sundae2]

    def deserts_count(self):
        return len(self.deserts)

    def total_cost(self):
        total_cost = 0
        for desert in self.deserts:
            total_cost += desert.get_cost()
        return total_cost

    def __str__(self):
        stt = {}
        for desert in self.deserts:
            stt[desert.name] = desert.get_cost()
        #
        stt2 = ''
        for item, cost in stt.items():
            stt2 = stt2 + "Deset: " + str(item) + "|| Cost: " + str(cost) + '\n'

        stt2 = stt2 + "Total Cost : " + str(self.total_cost())
        return stt2

check = Checkout()
print(check)