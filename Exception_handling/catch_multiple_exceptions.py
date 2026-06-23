##You can also catch multiple exceptions with separate except blocks:

try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number.')
except ZeroDivisionError:
    print("Can't divide by zero.")


##By using separate except clauses, you can make your error responses more
##specific and useful.
