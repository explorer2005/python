class animal:
    def __init__(self):
        print("I am constructor of animal class")

class landAnimals(animal):
    def __init__(self):
        super().__init__()
        print("I am constructor of landAnimals")

class dog(landAnimals):
    def __init__(self):
        super().__init__()
        print("I am constructor of dog class")

o=dog()