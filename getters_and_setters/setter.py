class Company:
    def __init__(self,com_name,modal_name):
        self.__company = com_name
        self.__modal = modal_name
    
    def company(self):
        return self.__company
    
    def modal(self):
        return self.__modal
    
    def set_company(self,modal):
        self.__modal = modal
    
car1 = Company('TATA','Siara')
print(car1.company())
print(car1.modal())
car1.set_company('Land Rover')
print(car1.company())
