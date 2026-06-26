##__add__ is a special magic method (also called a "dunder" method) used to
##implement operator overloading for the addition operator (+).

##When you write object1 + object2, Python automatically translates it under
##the hood into a method call: object1.__add__(object2)

#Program Two
class Concate:
    def __init__(self,name):
        self.name=name

    def __add__(self,other):
        return f'{self.name} {other.name}' 

fname = Concate('Saurabh')
lname = Concate('G. Pandey')

print(fname+lname)

# Program One
##class Math:
##    def __init__(self,a):
##         self.a=a
##         
##
##    def __add__(self,other):
##         return self.a+other.a
##
##
##math1 = Math(2)
##math2 = Math(5)
##
##print(math1+math2)
