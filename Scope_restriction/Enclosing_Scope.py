##Enclosing Scope: This is when a function that's nested inside another function
##can access the variables of the function it's nested within.

def outer_func():
    msg = 'Hello there!'
    
    def inner_func():
        print(msg)
    inner_func()

print(outer_func()) # Hello there!
