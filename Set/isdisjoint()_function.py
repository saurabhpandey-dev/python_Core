#.isdisjoint() method checks if two sets are disjoint, which means they
#don't have any elements in common.

my_set ={1,2,3,4,5}
your_set = {3,4,5,7}

print(my_set.isdisjoint(your_set))

your_set = {7,8,9,0}

print(my_set.isdisjoint(your_set))
