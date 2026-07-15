class A:
    a=10  # this is global variable
    _b=20 # this is protected variable access via create object or inherite class or class_name.protected_name
    __c=30 # this is private variable accesseble only in the class 
    # use name mangling for access outside from the class
    
    def showA(self):
        print('a :',self.a)
        print('b :',self._b)
        print('c :',self.__c)

class B(A):
    def showB(self):
        print('a :',self.a)
        print('b :',self._b)
        # print('c :',self.__c)  # here is the error becouse in parent class it is private variable
        
one = A()
one.showA()

two = B()
two.showB()


# print(obj.a)  #we can access all over the program
# print(obj._b)
# print(obj.__c)