import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(*num)

num.remove(2) # using remove function for remove any desired data from the array
print(*num)