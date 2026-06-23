##You can also use the exception object, which is typically aliased to another
##name with the as keyword. Here we're using e as an alias for the error object.

try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')

    
##Using e lets you access the actual error message or object for logging or
##debugging.
