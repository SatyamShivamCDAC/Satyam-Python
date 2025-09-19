

class Human:
    population = 0

    def __init__(self,name,age,gender):
        Human.population += 1

        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    def print_population():
        print('total population : ',str(Human.population))

    def die(self):
        Human.population -= 1
        self.__del__()

    def __del__(self):
        pass


    def __str__(self):
        return "Name : " + self.name




satyam = Human("Satyam",22,'male')
shivam = Human("Shivam",23,'male')
piyush = Human("Piyush",24,'male')

print(shivam)
shivam.die()
print(shivam)
Human.print_population()
