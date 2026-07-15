# A child class inherits from two or more parent classes.

class A:
    def name(self):
        print('Saurabh')

class B:
    def title(self):
        print('Pandey')

class C(A,B):
    def print_all(self):
        print('My name is Saurabh G. Pandey.')
        
obj = C()
obj.name()
obj.title()
obj.print_all()