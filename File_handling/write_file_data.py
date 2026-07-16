f = open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\ram.txt','w')
# here opened the file 'w' mode for write the data inside the file

f.write('I am the God \nName is Ganguly Bhaiya!') # data inside the quetes
# using .write() function for write the data inside the file 

print('file data write sucessfully.')
f.close()

# Agar aap 'w' (write) mode ka use karte hain, toh function jitni baar bhi run hoga, 
# wo purane data ko poori tarah override (delete) karke naya data likh dega.

# Agar aap chahte hain ki purana data delete na ho aur naya data uske neeche judta jaye, 
# toh aapko 'a' (append) mode ka use karna hoga.













