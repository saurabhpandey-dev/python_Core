class Car:
    def __init__(self,name,company):
        self.__name=name
        self.__company=company
        
    def name(self):  # here i create the getter methods
        return self.__name
    
    def company(self):
        return self.__company
    
car1 = Car('Esclade','Cadillac')    

print(car1.name()) # here call the getter method
print(car1.company())

print(car1.__name)  # error becouse __name is private
print(car1.__company) # error becouse __company is private