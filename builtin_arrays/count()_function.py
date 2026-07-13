import array as arr

num = arr.array('i',[1,2,3,4,5,6,7,5,3,8,5])
print(*num)

print(num.count(3)) # using count function for check the occurrence of passed argument
