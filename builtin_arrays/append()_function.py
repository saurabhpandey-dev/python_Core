import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(*num)

num.append(7) # using append function for insert new data on the last of the array
print(*num)