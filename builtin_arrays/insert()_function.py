import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(*num)

num.insert(4,3) # using insert function for insert new data on the desired position of the array
print(*num)