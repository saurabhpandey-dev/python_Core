import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(*num)

num.pop() # using pop function for remove data from the last of the array
num.pop()
num.pop(0) # pop function is also del data according to the given position parametar
num.pop(1)
print(*num)