# A child class inherits from two or more parent classes.

#parent class 1
class Ayush:
    f = 'Html, Css, JS'
    
    def front(self):
        print('ayush doing frontend, using : ',self.f)

#parent class 2
class Ananaya:
    b = 'mysql and python'
    
    def back(self):
        print('ananaya doing backend, using : ',self.b)
        
        #child class who inherite parent 1 and 2 both
class Saurabh(Ayush,Ananaya):  # here is saurabh is inherite ayush and ananaya 
    lead = 'asign task!'        # we can use multiple classes by comma sapreted
    def task(self):
        print(self.lead)
        self.front()
        self.back()
        
    def show(self):
        print('dynamic Web site creation.')

obj = Saurabh()

obj.show()
obj.task()
obj.back()
obj.front()