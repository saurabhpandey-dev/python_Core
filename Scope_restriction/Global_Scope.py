##Global Scope: This refers to variables that are declared outside any functions
##or classes which can be accessed from anywhere in the program.


tax = 0.70 

def get_total(subtotal):
    total = subtotal + (subtotal * tax)
    return total

print(get_total(100))  # 170.0
