f = open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\ram.txt','r')
# here opened the file 'r' mode for read the data from inside the exiting file

print(f.read()) # it's print all the of the file

print('file data read sucessfully.')

f.close()  # here we closed file 
print('File Closed!!')