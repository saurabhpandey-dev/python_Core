# tuple() function is used to Converts an iterable (like a list or string) into a tuple.

lst = ['ram', 25, 7.5] # this is the list 

print(lst) #['ram', 25, 7.5]
print(type(lst)) #<class 'list'>

tup = tuple(lst)
print(tup) #('ram', 25, 7.5)
print(type(tup)) #<class 'tuple'>