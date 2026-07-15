# A class acts as a parent for another class, which in turn acts as a parent
# for a third class, forming a chain.

class Father:
    fname = 'Rajeswar Prashad'
    sur = 'Pandey'
    def show_father(self):
        print(self.fname,self.sur)
    
class Son(Father):  # inherite the Father class
    sname = 'Markandey'
    def show_son(self):
        print(self.sname,self.sur)

class Gson(Son): # inherite the Son class
    name = 'Saurabh'
    def show_gson(self):
        print(self.name,self.sur)
        
    
        
obj1 = Gson()
obj1.show_gson() # but here we are using both data becouse of multilavel inheritence

obj2 = Son()
obj2.show_son()

obj3 = Father()
print(obj2.show_father()) # when we use double print funtion it can be print None also