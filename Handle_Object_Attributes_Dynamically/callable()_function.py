#The callable() function in Python is a built-in method used to determine
#if an object can be called like a function using parentheses ().
#It returns True if the object appears to be callable, and False if it is not.

def my_function():
    return "Hello"

number = 42

print(callable(my_function))  
print(callable(number)) 
