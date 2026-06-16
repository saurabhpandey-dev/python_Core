##The remove() method in Python deletes a specific element from a set in-place.
##If the item is found, Python updates the set; if the item does not exist,
##it immediately raises a KeyError

s1 = {1,2,3,4,5,6}
print(s1)
s1.remove(3)
print(s1)
s1.remove(8)
