from abc import ABC, abstractmethod

# Created an abstract class that inherits from ABC
class Car(ABC):
    
    # This is a normal method that will be inherited by all child classes
    def wheele(self):
        print('every car have 4 wheele!!')
    
    # This is an abstract method. It only contains a declaration,
    # and its implementation is mandatory for any child class
    @abstractmethod
    def speed(self):
        pass
    
# Maruti class inherits from the Car abstract class
class maruti(Car):
    
    # Here we implemented (overrode) the abstract method 'speed'
    def speed(self):
        print('speed 100')
    

# Created an object of the Maruti class
obj = maruti()

# Calling the normal method from the Car class
obj.wheele()

# Calling the implemented speed method from the Maruti class
obj.speed()