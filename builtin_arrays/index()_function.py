import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(*num)

print(num.index(5)) # using index function for check the index of passed argument
