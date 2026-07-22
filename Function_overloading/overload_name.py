class names:

    def show():
        print('Name not defined')
    
    def show(first='pta nhi'):
        print(f'{first}')
    
    def show(first='',second=''):
        print(f'{first} {second}')

obj = names

obj.show()
obj.show('Saurabh')
obj.show('saurabh','pandey')
# Is this is a function/method overloading ?

# No, this is not method overloading.

# In Python, defining multiple functions or methods with the same name 
# in the same scope does not overload them. Instead, the Python interpreter
# simply overwrites the previous definitions.

# The last def show(first='', second='') will be the only one that exists 
# in memory.Calling obj.show(), obj.show('Saurabh'), and 
# obj.show('saurabh', 'pandey') will execute the final method three times,
#  utilizing default parameters and printing