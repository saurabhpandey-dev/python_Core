import copy

original = [[10 , 20],[30 , 40]]
print(f'original : {original}')

sallow = copy.copy(original)
print(f'sallow : {sallow}')

sallow [0][0] = 5

print(f'original after sallow : {original}')  # here sallow change the original

deep = copy.deepcopy(original)
print(f'deep : {deep}')

deep[0][1] = 15
print(f'after deepcopy : {deep}')

print(f'original after deepcopy : {original}')  # here deepcopy not change the original


# Shallow copy (copy.copy() ya list[:]) sirf outer object ka naya copy banata hai, lekin andar ke nested objects 
# same reference share karte hain. Deep copy (copy.deepcopy()) recursively har nested object ka bhi naya 
# independent copy banata hai.

