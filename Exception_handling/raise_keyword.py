##the raise statement is a powerful tool that allows you to manually trigger
##exceptions in your code. It gives you control over when and how errors are
##generated, enabling you to create custom error conditions and enforce specific
##program behavior.
##
##The raise statement is used to explicitly throw an exception at any point in
##your program, allowing you to signal that an error condition has occurred or
##that certain requirements haven't been met.
##
##Python's raise statement can be used in several ways to trigger exceptions.
##At its most basic, you can raise built-in exceptions or create custom error
##messages.

def check_age(age):
    if age<0:
        raise ValueError ('minus na chali beta')
    return age

try:
    check_age(-1)
except ValueError as e:
    print(f'Error : {e}')
