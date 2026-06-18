##The symmetric difference operator ^ returns a new set with the elements that
##are either in the first or the second set, but not both. In this case, 1 and 5
##are in my_set but not in your_set, so they are included. And the
##number 6 is in your_set but not in my_set, so it's included as well


myset = {1,2,3,4,5}
yourset = {5,6,7,8,9}

print(myset ^ yourset)
