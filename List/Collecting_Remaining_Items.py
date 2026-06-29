#Collecting Remaining Items From a List: To collect any remaining elements
#from a list, you can use the asterisk (*) operator like this.


developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name)
print(rest)
