class Dog:
    def __init__(self,name):
        self.name=name
        

    def display(self):
        print(f'{self.name} says woof woof!')


dog1 = Dog('sheru')
dog2 = Dog('lushi')

dog1.display()
print(dog2.display)  # if i don't give () the it return location of memory address
print(dog2)  # same both are return same object address

