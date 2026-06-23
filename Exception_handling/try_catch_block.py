##Exception Handling is a core part of writing robust and fault-tolerant programs.
##It allows you to anticipate, catch, and respond to errors in a structured way.
##Exception handling is the process of catching and managing errors that occur
##during the execution of a program, so your code doesn't crash unexpectedly.

try:
    x = 10/0
except ZeroDivisionError:
    print('value could not be divided by zero')


##try: The block of code where you anticipate an error might occur.
##
##except: This block runs if an error of the specified type is raised inside
##the try block.
##
##In this case, dividing by zero raises a ZeroDivisionError, which is then
##caught and handled.
