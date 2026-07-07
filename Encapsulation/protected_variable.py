# A protected variable is written with a single leading underscore.

# The Rule: It serves as a gentle warning to other developers that the variable is intended for 
# internal use within the class and its child classes.

# The Reality: Python does absolutely nothing to stop you from accessing or modifying it from
# outside the class.

class Parent:
    def __init__(self):
        self._protected_var = "I am protected"

obj = Parent()
# This works, but it is highly discouraged by convention
print(obj._protected_var)  # Output: I am protected
