# A private variable is written with a double leading underscore.
# The Rule: It indicates that the variable should only be accessible within the specific class where it was defined.
# The Reality: Python applies a mechanism called Name Mangling. It automatically rewrites the internal name behind 
# the scenes so that direct external calls fail with an AttributeError.

class Parent:
    def __init__(self):
        self.__private_var = "I am private"

obj = Parent()

# This will fail!
# print(obj.__private_var)  # Raises AttributeError

# How to bypass it using Name Mangling:
# Python rewrote the variable to: _ClassName__variableName
print(obj._Parent__private_var)  # Output: I am private
