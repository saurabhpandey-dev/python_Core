from abc import ABC, abstractmethod

#subclasses can override methods declared in a parent class to supply localized logic.

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print('Woof Woof!!')

class Cat(Animal):

    def sound(self):
        print('Meow Meow!!')


dog = Dog()
cat = Cat()


dog.sound()
cat.sound()