f = open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\ram.txt','r')
# here opened the file 'r' mode for read the data from inside the exiting file

print(f.readlines()) # it's print all lines of the file but in list form
f.close()

# ex:
#     ['I am the God \n', 'Name is Ganguly Bhaiya!']