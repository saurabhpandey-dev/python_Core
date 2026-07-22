from abc import ABC,abstractmethod

class Vahical(ABC):

    # interface is normal abstract method but just a difference is the you can not 
    # define the body in abstracted class only abstract method is existed in class.
    
    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def engine(self):
        pass 

    @abstractmethod
    def type(self):
        pass

class car(Vahical):

    def name(self): # this is not a interface inherited function
        print('Land Rover Defendar')

    # if you were forget or not created the abstrected method in child class 
    # you will got TypeError 
    # hence, you must be created abstracted function who only define in abstract class.

    def speed(self):
        print('car max speed is 250 km/h')
    
    def engine(self):
        print('2.0 litre turbo charged V6 inline')
    
    # if you can not create the abstract method you got method
    # def type(self):  
    #     print('car type is SUV')  


obj = car()

obj.name()
obj.speed()
obj.engine()
obj.type()


# interface Vs Abstraction
# interface
# Jab sirf ye fix karna ho ki methods kaun-kaun se honge.	

#abstraction
# Jab methods ke sath-sath kuch common functionality bhi saare objects
#  ko deni ho.