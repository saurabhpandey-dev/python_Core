import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(*num)

num.extend([4,3]) # using extend function for insert new list of data on the array
print(*num)
