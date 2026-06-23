##You can also catch multiple exceptions in a single except clause by specifying
##the exceptions as a tuple:

try:
    x= int(input("Enter the number : "))
    y = x/0
except (ValueError,ZeroDivisionError) as e:
     print(e)


##Exception handling allows your programs to recover from errors gracefully.
##By using try, except, else, and finally, you can anticipate potential issues
##and build more resilient applications.
