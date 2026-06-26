class Car:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def display(self):
        print(f'your car is {self.color} color {self.name} modal')



car1 = Car('Caddillac','Black')
car2 = Car('Defender','Black')

car1.display()
car2.display()


##def __init__(self, name, age) is the special method automatically called
##when a new object is created. It initializes the attributes of the objects
##that will be created with the class.
##
##In addition to that, the first parameter of __init__ is always a reference
##to the specific object being created or used. By convention, this parameter
##is named self, but technically, you can use any name. self lets you access
##the object's own attributes and methods.
##
##self.name = name and self.age = age are the attributes the objects will have.
