# Method Overriding is a feature that allows a subclass (child class) to 
# provide a specific implementation of a method that is already defined in 
# its superclass (parent class).When a method in the child class has the 
# same name, same parameters, and same return type as a method in its parent
# class, the child class's method overrides (or takes precedence over) the 
# parent's method.

# Core Concept: How It Works

# When you call an overridden method on an instance of the child class, Python:
#     Checks if the method exists in the child class.
#     If it does, it executes the child's version.
#     If it doesn't, it looks up the inheritance tree and executes the parent's 
#     version.

class A:
    def show(self):
        print('user not defind name')

class B(A):
    def show(self,name=''):
        if name == '':
            super().show()
            return
        else:
            print(f'ich bin {name}')

obj = B()

obj.show() #user not defind name 

obj.show('Saurabh')  # ich bin saurabh


# class A:
#     def show(self):
#         print('user not defind name')

# class B(A):
#     def show(self,name=''):
#         print(f'my name is {name}')

# obj = B()

# obj.show() #user not defind name 

# obj.show('Saurabh') 