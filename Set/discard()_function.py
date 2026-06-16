##The discard() method in Python removes a specified element from a set if it
##exists, without raising an error if the element is missing. This makes it a
##safer option for element deletion compared to other built-in alternatives.

s1 = {1,2,3,4,5,6,7}
print(s1)
s1.discard(4)
print(s1)
s1.discard(9)
print('here is no error give back after not found the value')
