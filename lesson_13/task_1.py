from random import randint


class City:
    def __init__(self, name, streets=[]):
        self.name = name
        self.streets = streets

    def generate(self):
        for i in range(randint(20, 40)):
            self.streets.append(Street(i))
        for i in self.streets:
            i.generate()


class Street:
    def __init__(self, name, houses=[]):
        self.name = name
        self.houses = houses

    def generate(self):
        for i in range(randint(5, 20)):
            self.houses.append(House(i))
        for i in self.houses:
            i.generate


class House:
    def __init__(self, name, people=0):
        self.name = name
        self.people = people

    def generate(self):
        self.people = randint(1, 100)

