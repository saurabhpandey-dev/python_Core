##Sets are one of built-in data structures. One of the core
##characteristics of sets is that they don't store duplicate values.

##If you try to add a duplicate value to a set, only one of them will be stored.

##Sets are mutable and unordered, which means that their elements are not
##stored in any specific order, so you cannot use indices or keys to access them.

##They can only contain values of immutable data types like numbers,
##strings, and tuples. And they support mathematical set operations, including
##union, intersection, difference, and symmetric difference.

##To define a set, you just need to write its elements within curly braces
##and separate them with commas. 

s1 = {1,2,3,4,5,6}
s2 = {2,3,4,5}
print(s1)
print(type(s1))

s3 = (1,2,3,4,5)
print(s3)
print(type(s3))


s4 = set(s3)
print(type(s4))
print(s4)
