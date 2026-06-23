##And here's an example also showing how to use the else and finally blocks:


try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs.')



##else: Runs if no exception is raised in the try block.
##finally: Runs no matter what, whether or not an exception occurred.
##Useful for clean-up tasks like closing files or releasing resources.
