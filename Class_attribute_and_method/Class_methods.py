##Methods are functions defined inside a class. With them, any object defined
##from a class can perform actions that operate on or modify its own data.
##You also access a method with dot notation.


class Car:

    def __init__(self,name,color):
        self.name=name
        self.color=color

    def display(self): # this is a method/function which is created inside class
        print(f'your car is {self.color} {self.name}')


car1 = Car('Caddilac','Black')
car2 = Car('Defender','Black')

car1.display()
car2.display()
