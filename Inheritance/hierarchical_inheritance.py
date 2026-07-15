# Multiple child classes inherit from a single base parent class.

class Parent:
    p_data = 'Parent data'

class Child1 (Parent): # inherite Parent class
    c1_data = 'Child One'

class Child2 (Parent): # inherite Parent class
    c2_data = 'Child Two'
    
    
obj1 = Parent()
obj2 = Child1()
obj3 = Child2()

print(obj1.p_data)
print(obj2.c1_data)
print(obj3.c2_data)
