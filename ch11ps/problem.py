# class TwoVector:
#     def __init__ (self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f"Two D Vector is {self.i}i+{self.j}j)")

# class ThreeVector(TwoVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f"Three D Vector is {self.i}i+{self.j}j+{self.k}k")

# a=TwoVector(3,4)
# b=ThreeVector(3,4,5)
# a.show()
# b.show()

class Animals:
    def __init__(self):
        print("I am Animal class")

class Pets(Animals):
    def __init__(self):
        super().__init__()
        print("I am pet class")

class Dog(Pets):
    def __init__(self):
        super().__init__()
        print("I am Dog class ")

a=Dog()