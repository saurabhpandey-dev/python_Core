class Cars:
    company = 'TATA'

    def __init__(self,modal,color):
        self.name=modal
        self.color=color

    def __str__(self):
        return f'your ccar is {self.color} color {self.name}'


car1 = Cars('Siara', 'Mochha Green')

print(Cars.__dict__) # it will print all staff of object in dictionary 
print(car1.__dict__) # it will print only print car1 dictionary

