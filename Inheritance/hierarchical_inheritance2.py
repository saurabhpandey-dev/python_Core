class Father:
    f_name ='Markandey'
    sur = 'Pandey'
    def p_name(self):
        print(self.f_name,self.sur)

class Sunil(Father):
    s_name = 'Sunil'
    def d_name(self):
        print(self.s_name,self.sur)
            
class Saurabh(Father):
    s_name = 'Saurabh G.'
    def d_name(self):
        print(self.s_name,self.sur)

obj1 = Father()
obj2 = Sunil()
obj3 = Saurabh()

obj1.p_name()
obj2.d_name()
obj3.d_name()