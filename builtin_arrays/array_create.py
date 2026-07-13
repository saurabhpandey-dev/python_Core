import array as arr  # here we need to import the array module

num = arr.array('i',[1,2,3,4,5,6]) 
# we need to create an array using the .array('i',[1,2,3,4,5]) function 
# in array() function 'i' means integer 'f' means float and after comma we insert [squat bracket]
# for insert data
print(num ) # here print the whole method array('i', [1, 2, 3, 4, 5, 6])
print(*num) # we use * for print only data otherwise it print whole function