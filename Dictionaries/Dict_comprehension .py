# Same list jaisa syntax bas {} brackets aur key:value pattern ke saath.

square = {x:x*x for x in range(10)} # return square of all 0 to 9 number 

print(square) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# find unique length 
unique_lengths = {len(word) for word in ["cat", "dog", "elephant"]}
print(unique_lengths) # {3, 8}
