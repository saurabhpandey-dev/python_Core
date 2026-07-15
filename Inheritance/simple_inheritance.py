class Father :  # this is a parent class
    def lands(self):
        print('father have 50 bigha land')
        
class Son(Father): # this is a child class
    def money(self):
        print('son have 1cr money')

son = Son()
son.money()
son.lands()

# A child class inherits from exactly one parent class.